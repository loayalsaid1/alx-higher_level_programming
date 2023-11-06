#include "lists.h"

/**
 * second_list_half - get start of the seconde half of a list
 * @head: a pointer to the head of list
 * Return:  The first node
 */
listint_t *second_list_half(listint_t *head)
{
	listint_t *fast = head, *slow = head;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	if (fast != Null)
		return (slow.next);
	else
		return (slow);
}

