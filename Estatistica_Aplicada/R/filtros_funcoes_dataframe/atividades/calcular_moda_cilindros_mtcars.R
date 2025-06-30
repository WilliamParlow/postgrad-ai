# Implementar um script usando a linguagem R para calcular a moda em 
# relação ao número de cilindros do mtcars

# Calculates the mode of a vector.
#
# unique(v)     -> Returns a vector with only unique elements from 'v' (removes duplicates).
# match(v, un_v) -> Returns a vector of the positions (indices) of the elements of 'v'
#                   within the 'un_v' (unique values) vector. For example, if v = c(1, 2, 1)
#                   and un_v = c(1, 2), then match would return c(1, 2, 1).
# tabulate()    -> Counts the occurrences of each integer in its input. When used with
#                   the output of 'match', it effectively counts how many times each
#                   unique value appears in the original vector 'v'.
# which.max()   -> Returns the index (position) of the largest value in a numeric vector.
#                   In this context, it finds the index of the unique value that appears
#                   most frequently.
# return(un_v[]) -> Returns the unique value itself, using the index found by 'which.max'.
#                   This unique value is the mode because it's the one that occurred most often.
moda = function(v) {
  un_v = unique(v)
  return(un_v[which.max(tabulate(match(v, un_v)))])
}

moda(mtcars$cyl)
