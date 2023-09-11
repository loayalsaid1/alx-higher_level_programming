#include "lists.h"

/**
 * insert_node - insert a node inside a sorted linked list in the write place
 * @head: a pointer to the head pointer
 * @number: and number to feed the number to feed the node
 * Return: the address of the created node if the process succeds
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *node;

	node = malloc(sizeof(listint_t));
	if (node == NULL)
		return (NULL);

	node->n = number;
	node->next = NULL;

	if (*head == NULL)
	{
		*head = node;
		return (node);
	}

	current = *head;
	
	if (node->n <= current->n)
	{
		node->next = *head;
		*head = node;
		return (node);
	}


	while (current->next != NULL)
	{
		if (node->n <= current->next->n)
		{
			node->next = current->next;
			current->next = node;
			return (node);
		}

		current = current->next;
	}
	current->next = node;

	return (node);
}
