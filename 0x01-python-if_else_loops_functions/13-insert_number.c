#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer of the head of the list
 * @number: the number to be inserted
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newNode = malloc(sizeof(listint_t));
	listint_t *current;

	if (newNode == NULL)
		return (NULL);
	newNode->n = number;
	newNode->next = NULL;
	if (*head == NULL || number < (*head)->n)
	{
		newNode->next = *head;
		*head = newNode;
	}
	else
	{
		current = *head;
		while (current->next != NULL && number > current->next->n)
			current = current->next;
		newNode->next = current->next;
		current->next = newNode;
	}

	return (newNode);
}
