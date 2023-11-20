#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <floatobject.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: a PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int allocated, size, i;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	setbuf(stdout, NULL);
	allocated = list->allocated;
	size = ((PyVarObject *) p)->ob_size;

	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
		else if (strcmp(type, "float") == 0)
			print_python_float(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	int i, size = ((PyVarObject *)p)->ob_size;
	PyBytesObject *bytes = (PyBytesObject *)p;

	setbuf(stdout, NULL);
	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", bytes->ob_sval);

	if (size > 10)
		size = 10;
	else
		size = size + 1;

	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", bytes->ob_sval[i]);
		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

/**
 * print_python_float - print baisc info about float object
 * @p: pyobject
 * Return: nothing
 */
void print_python_float(PyObject *p)
{
	PyFloatObject *f = (PyFloatObject *)p;

	setbuf(stdout, NULL);
	printf("[.] float object info\n");
	if (strcmp(p->ob_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("  value: %s\n", PyOS_double_to_string(f->ob_fval
	, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}
