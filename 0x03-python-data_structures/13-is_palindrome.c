#include "lists.h"

/**
* is_palindrome - Checks if a singly linked list is a palindrome.
*
* @head: pointer to the first node of the list.
*
* Return: 0 if it is not a palindrome, 1 if it is a palindrome.
*/
int is_palindrome(listint_t **head)
{
	listint_t *tail;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tail = *head;

	while (tail->next)
		tail = tail->next;

	while (*head)
	{
		if (*head == tail)
			break;

		if ((*head)->n != tail->n)
			return (0);

		*head = (*head)->next;
		tail = tail->prev;
	}

	return (1);
}

/**
 * reverse_listint - reverses a listint_t linked list.
 *
 * @head: pointer to the head of the list.
 *
 * Return: a pointer to the first node of the reversed list.
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *next = NULL;
	listint_t *prev = NULL;

	if (!head || !*head)
		return (NULL);

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;

	return (*head);
}
