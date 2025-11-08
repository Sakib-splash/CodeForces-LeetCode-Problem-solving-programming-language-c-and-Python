def is_prime(num)
{
  if num<=1:
    return False
  if num % 2 ==0:
    return False
  if num == 2:
    return True
  for i in range(3,int(math.sqrt(num))+1, 2):
    if num % i == 0:
      return False

return True
}
num = int(input())
if is_prime(num):
  print(f"The number {num} is a prime number")
else:
  print(f"The number {num} is not  a Prime number)
  
