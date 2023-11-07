#include "Python.h"
#include <stdio.h>

/**
 * print_python_list_info - print an info about a python list object
 * @p: the python object
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	int size, allocated, i;

	size = Py_SIZE(list);
	allocated = list->allocated;

	printf("[*] Size of the Python List = %i\n", size);
	printf("[*] Allocated = %i\n", allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %i: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
	}
}
