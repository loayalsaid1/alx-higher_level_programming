#include "lists.h"

/**
 * is_palindrome - check for palindrome in a singly linked list
 * @head: a double pointerr to the head of the list
 * Return: 0 if not and 1 if there is a palindrom
 */
int is_palindrome(listint_t **head)
{
	/*
	 * :becaseu this is c89 i cant create an array in the iddle
	 * of the code, so i created an array of 100 for now
	 */
	int arr[1000000];
	listint_t *current;
	int i = 0;
	int j = 0;

	if (!head || !*head)
		return (1);

	current = *head;
	while (current != NULL)
	{
		arr[i] = current->n;
		i++;
		current = current->next;
	}

	while (i > j)
	{
		if (arr[i] != arr[j])
			return (0);
	}

	return (1);
}
