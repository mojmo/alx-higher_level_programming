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

	tail = *head;

	while (tail->next)
		tail = tail->next;

	if (*head == NULL || *head == tail)
		return (1);

	return (is_palindrome_helper(*head, tail));
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
	if (head == NULL || head == tail || tail == NULL)
		return (1);

	if (is_palindrome_helper(head->next, tail - 2) && head->n == tail->n)
		return (1);

	return (0);
}
