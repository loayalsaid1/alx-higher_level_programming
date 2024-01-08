#include <stdio.h>
#include <string.h>
#include <Python.h>
#include <unicodeobject.h>

/**
 * print_python_string - print a string whther ascii or unicode
 * @p: the pyoject
 * Return: void
*/
void print_python_string(PyObject *p)
{
	PyUnicodeObject *str = (PyUnicodeObject *) p;

	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(str))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %ls\n", PyUnicode_AS_UNICODE(p));
}
