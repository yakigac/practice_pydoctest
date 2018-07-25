def fizzbuzz(n):
    '''
    FizzBuzz
    The code from: https://blog.amedama.jp/entry/2016/01/25/212244

      >>> from fizzbuzz import fizzbuzz
      >>> fizzbuzz(2)
      '2'
      >>> fizzbuzz(3)
      'Fizz'
      >>> fizzbuzz(4)
      '4'
      >>> fizzbuzz(5)
      'Buzz'
      >>> fizzbuzz(6)
      'Fizz'
      >>> fizzbuzz(7)
      '7'
      >>> fizzbuzz(14)
      '14'
      >>> fizzbuzz(15)
      'FizzBuzz'
      >>> fizzbuzz(16)
      '16'

    '''
    if n % 3 == 0 and n % 5 == 0:
        return 'FizzBuzz'

    if n % 3 == 0:
        return 'Fizz'

    if n % 5 == 0:
        return 'Buzz'

    return str(n)
