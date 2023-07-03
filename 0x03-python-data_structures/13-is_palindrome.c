#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - reverses a linked list
 * @head: double pointer to the head of the list
 * Return: pointer to the new head of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *current = *head;
	listint_t *next;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}

/**
 * check - checks if two linked lists are equal
 * @list1: double pointer to the head of the first list
 * @list2: double pointer to the head of the second list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int check(listint_t **list1, listint_t **list2)
{
	while (*list1 != NULL && *list2 != NULL)
	{
		if ((*list1)->n != (*list2)->n)
		{
			return (0);
		}
		*list1 = (*list1)->next;
		*list2 = (*list2)->next;
	}
	return (*list1 == NULL && *list2 == NULL);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if the list is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *second_half;
	listint_t *prev_of_slow_ptr = *head;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		prev_of_slow_ptr = slow_ptr;
		slow_ptr = slow_ptr->next;
	}
	if (fast_ptr != NULL)
		second_half = slow_ptr->next;
	else
		second_half = slow_ptr;
	prev_of_slow_ptr->next = NULL;
	second_half = reverse_list(&second_half);
	is_palindrome = check(head, &second_half);
	second_half = reverse_list(&second_half);
	if (fast_ptr != NULL)
	{
		prev_of_slow_ptr->next = slow_ptr;
		slow_ptr->next = second_half;
	}
	else
		prev_of_slow_ptr->next = second_half;

	return (is_palindrome);
}
