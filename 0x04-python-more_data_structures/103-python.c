#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists.
 * @p: a PyObject list object.
 */
void print_python_list(PyObject *p)
{
	int allocated, size, i;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	allocated = list->allocated;
	size = ((PyVarObject *) p)->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		type = list->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[i]);
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects.
 * @p: A PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	int i, size = ((PyVarObject *)p)->ob_size;
	PyBytesObject *list = (PyBytesObject *)p;

	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("[.] bytes object info\n");
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", list->ob_sval);

	if (size > 10)
		size = 10;
	else
		size = size + 1;
	printf("  first %d bytes: ", size);
	for (i = 0; i < size; i++)
	{
		printf("%02hhx", list->ob_sval[i]);

		if (i == (size - 1))
			printf("\n");
		else
			printf(" ");
	}
}

