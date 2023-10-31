#include "lists.h"
#include <stdlib.h>

/**
* insert_node - inserts a number into a sorted singly linked list.
*
* @head: pointer to the first node of the linked list.
* @number: the value of the new node.
*
* Return: the address of the new node, or NULL if it failed.
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *slow, *fast;
	listint_t *new_node = malloc(sizeof(listint_t));
	new_node->n = number;
	new_node->next = NULL;

	if (head == NULL)
	{
		new_node->next = NULL;
		*head = new_node;
		return (new_node);
	}

	slow = *head;
	fast = (*head)->next;

	while (slow != NULL && fast != NULL)
	{
		if (number >= slow->n && number <= fast->n)
		{
			slow->next = new_node;
			new_node->next = fast;
			return (new_node);
		}
		if (number > fast->n && fast->next == NULL)
			fast->next = new_node;

		slow = slow->next;
		fast = fast->next;
	}

	free_listint(new_node);
	return (NULL);
}
