#include <Python.h>

/**
 * print_python_bytes - Print some basic info about Python lists
 * and Python bytes objects.
 *
 * @p: a pointer to a Python object
 *
 * Return: Nothing
 */
void print_python_bytes(PyObject *p)
{
	int i, size;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %d\n", size);
	printf("  trying string: %s\n", str);

	if (size < 10)
		printf("  first %d bytes: ", size + 1);
	else
		printf("  first 10 bytes: ");

	for (i = 0; i <= size && i < 10; i++)
	{
		printf("%02hhx", str[i]);
		if (i < size && i < 9)
			printf(" ");
	}
	printf("\n");
}


/**
 * print_python_list - Print some basic info about Python
 *lists and Python bytes objects.
 * @p: a pointer to a Python object
 *
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	int i, size, allocated;
	PyObject *element;
	const char *type;

	printf("[*] Python list info\n");

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		type = Py_TYPE(element)->tp_name;

		printf("Element %d: %s\n", i, type);

		if (PyBytes_Check(element))
			print_python_bytes(element);
	}
}
