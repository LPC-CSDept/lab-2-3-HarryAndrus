def main():
    val1 = int(input('What is the First integer? '))
    val2 = int(input('What is the Second integer? '))
    val3 = int(input('What is the Third integer? '))
    sum = (val1+val2+val3)
    avg = (sum / 3)
    print('Values:',val1,val2, val3)
    print(f'Total: \t {sum:.2f}')
    print(f'Average: {avg:.2f}')


if __name__ == '__main__':
    main()
