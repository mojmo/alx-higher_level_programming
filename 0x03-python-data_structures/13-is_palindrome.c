#include "lists.h"
#include <stdio.h>

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
	int len = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	tail = *head;

	while (tail->next)
	{
		++len;
		tail = tail->next;
	}

	if (len == 1 && (*head)->n == tail->n)
		return (1);

	return  (is_palindrome_helper(*head, tail));
}

/**
 * is_palindrome_helper - help to check if a string is palindrome or not.
 *
 * @head: pointer to the first node of the list.
 * @tail: pointer to the last node of the list.
 *
 * Return: 1 if s is palindrome, 0 if n not.
 */
int is_palindrome_helper(listint_t *head, listint_t *tail)
{
	if (!head  || (head == tail && head->n == tail->n) || !tail)
		return (1);

	if (head->n != tail->n)
		return (0);

	return (is_palindrome_helper(head->next, tail - 2));
}
