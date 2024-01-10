#include "execution.h"

int	str_table_get_size(char **str_table)
{
	int	i;

	i = 0;
	if (!str_table)
		return (0);
	while (str_table[i])
		i++;
	return (i);
}

t_str_table	str_table_init(int size)
{
	t_str_table	str_table;
	char		**table;
	int			i;

	i = 0;
	str_table.size = size;
	str_table.table = (char **)malloc(sizeof(char *) * (str_table.size + 1));
	if (!str_table.table)
		return (str_table);
	while (i < size + 1)
	{
		str_table.table[i] = NULL;
		i++;
	}
	return (str_table);
}

int	str_table_cpy(t_str_table src, t_str_table dst)
{
	int	i;

	i = 0;
	if (src.size > dst.size)
		return (1);
	while (i < src.size)
	{
		dst.table[i] = src.table[i];
		i++;
	}
	return (0);
}

int	str_table_add_line(t_str_table *str_table, char *line)
{
	t_str_table	new_str_table;

	new_str_table = str_table_init(str_table->size + 1);
	if (!new_str_table.table)
		return (1);
	if (str_table_cpy(*str_table, new_str_table))
		return (1);
	new_str_table.table[str_table->size] = line;
	free(str_table->table);
	*str_table = new_str_table;
	return (0);
}

void	str_table_print(t_str_table str_table)
{
	int	i;

	i = 0;
	while (i < str_table.size)
	{
		printf("%d : %s\n", i, str_table.table[i]);
		i++;
	}
}

void	str_table_destroy(t_str_table str_table)
{
	int	i;

	i = 0;
	while (i < str_table.size)
	{
		free(str_table.table[i]);
		i++;
	}
	free(str_table.table);
}

int	main(void)
{
	t_str_table first_table;
	char		*line;
	int	i = 0;

	first_table = str_table_init(4);
	while (i < 4)
	{
		line = readline("> ");
		first_table.table[i] = line;
		i++;
	}
	str_table_print(first_table);
	line = readline("> ");
	str_table_add_line(&first_table, line);
	str_table_print(first_table);
	str_table_destroy(first_table);
}
