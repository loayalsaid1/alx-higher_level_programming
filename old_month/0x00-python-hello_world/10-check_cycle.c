#include "lists.h"

/**
 * check_cycle - check for existence of a cycle in a linked list
 * @list: a pointer to the first node
 * Return: 1 if a cycle exists and 0 if not;
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
