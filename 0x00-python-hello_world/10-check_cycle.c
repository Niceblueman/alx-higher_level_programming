#include "lists.h"

/**
 * check_cycle - a function in C that checks if a singly
 * linked list has a cycle in it
 * @list: pointer to a pointer of the start of the list
 * Return: 1 if does and 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}
