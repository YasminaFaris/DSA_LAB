"""sSwapVar"""
def convert_string_to_tuples(text_in):
  """SwapVar"""
  values = text_in.strip('()').split(', ')
  return tuple(map(float, values))

laongdao_data = convert_string_to_tuples(input())
print(tuple(reversed(laongdao_data)))
