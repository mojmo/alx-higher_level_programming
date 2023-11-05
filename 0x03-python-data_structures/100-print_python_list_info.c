#include <Python.h>
#include <listobject.h>
#include <object.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 *
 * @p: a pointer to a Python object.
 *
 * Return: Nothing.
 */
void print_python_list_info(PyObject *p)
{
	int i;
	int size = PyObject_Size(p);
	int allocated_size = ((PyListObject *)p)->allocated;
	pyObject *element;
	char *type;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated_size);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		type = Py_TYPE(element)->tp_name;

		printf("Element %d: %s\n", i, type_name);
	}
}
