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

	if (fast != NULL)
		return (slow->next);
	else
		return (slow);
}

/**
 * reverse_list - reverse the direction of a singly linked list
 * @head: the head of the linked list
 * Return: the last node of the list(the first of the new one)
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *head_next, *new_head;

	if (head == NULL || head->next == NULL)
		return (head);
	new_head = reverse_list(head->next);
	head_next = head->next;
	head_next->next = head;
	head->next = NULL;

	return (new_head);
}

/**
 * is_palindrome - check for palindrome in a linked list
 * @head: a double pointer to the head
 * Return: 1 if true, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *start = *head, *mid, *last;

	if (head == NULL || *head == NULL)
		return (1);

	mid = second_list_half(*head);
	last = reverse_list(mid);

	while (last != NULL)
	{
		if (last->n != start->n)
			return (0);
		last = last->next;
		start = start->next;
	}
	return (1);
}
