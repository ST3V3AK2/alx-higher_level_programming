#include "lists.h"
#include <stdio.h>
#include <unistd.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: input linked list
 *
 * Return: 0 if there are no cycles
 * 1 if there i a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *temp;

	current = list;
	temp = list;
	while (current != NULL)
	{
		current = current->next;
		if (temp == current)
			return (1);
	}
	return (0);
}
