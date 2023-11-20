#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - Print information about a Python bytes object
 * @p: Pointer to the Python bytes object
 *
 * This function prints information about a Python bytes object, including
 * its size, first 10 bytes in hexadecimal, and a string representation.
 * If the given object is not a valid bytes object, an error message is
 * printed.
 *
 * Return: void.
 */
void print_python_bytes(PyObject *p)
{
	long int i, size;
	char *str;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		setbuf(stdout, NULL);
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
	setbuf(stdout, NULL);
}

/**
 * print_python_float - Print information about a Python float object
 * @p: Pointer to the Python float object
 *
 * This function prints information about a Python float object, including
 * its value. If the given object is not a valid float object, an error
 * message is printed.
 *
 * Return: void.
 */
void print_python_float(PyObject *p)
{
	double value;
	char *num_buf;

	setbuf(stdout, NULL);

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		setbuf(stdout, NULL);
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	num_buf = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0,
			Py_DTST_FINITE);

	printf("  value: %s\n", num_buf);
	setbuf(stdout, NULL);
	PyMem_Free(num_buf);
}

/**
 * print_python_list - Print information about a Python list object
 * @p: Pointer to the Python list object
 *
 * This function prints information about a Python list object, including its
 * size, allocated space, and details about each element. If an element is a
 * bytes or float object, additional information about the specific type is
 * printed using dedicated functions.
 *
 * Return: void.
 */
void print_python_list(PyObject *p)
{
	long int i, size, allocated;
	PyObject *element;

	setbuf(stdout, NULL);

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		setbuf(stdout, NULL);
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		element = ((PyListObject *)p)->ob_item[i];

		printf("Element %ld: %s\n", i, element->ob_type->tp_name);

		if (PyBytes_Check(element))
			print_python_bytes(element);

		if (PyFloat_Check(element))
			print_python_float(element);
	}
	setbuf(stdout, NULL);
}
