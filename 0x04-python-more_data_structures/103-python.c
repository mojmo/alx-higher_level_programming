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
	long int i, size;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %ld bytes: ", (size > 10 ? 10 : size + 1));

	for (i = 0; i <= size && i < 10; i++)
	{
		printf("%02x", (unsigned char)str[i]);
		if (i < size && i < 9)
			printf(" ");
	}
	printf("\n");
}

/**
 * print_python_list - Print some basic info about Python
 * lists and Python bytes objects.

 * @p: a pointer to a Python object
 *
 * Return: Nothing
 */
void print_python_list(PyObject *p)
{
	long int i, size, allocated;
	PyObject *element;

	size = ((PyVarObject *)p)->ob_size;
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		element = ((PyListObject *)p)->ob_item[i];

		printf("Element %ld: %s\n", i, element->ob_type->tp_name);

		if (PyBytes_Check(element))
			print_python_bytes(element);
	}
}
