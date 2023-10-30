#include "lists.h"

/**
 * check_cycle - a function in C that checks if a singly linked list has
 * a cycle in it.
 *
 * @list: a pointer to the linked list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	fast = list->next;
	while (fast != NULL)
	{
		if (fast == fast->next)
			return (1);

		slow = list;
		while (slow != fast)
		{
			if (slow == fast->next)
				return (1);

			slow = slow->next;
		}

		fast = fast->next;
	}

	return (0);
}
