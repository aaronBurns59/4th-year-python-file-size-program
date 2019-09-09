# Constant that holds the prefixes of file sizes in bytes
SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}

# function that approximates the size of the file given
def approx_size(size, a_kilobyte_is_1024_bytes = True):
    # if statement to check the size is not a positive number
    if size < 0:
        raise ValueError('Number entered must be positive')

    # sets multiple to 1024 if the above second argument is true
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    # a for loop that determines the suffix the value entered in size will get
    for suffix in SUFFIXES[multiple]:
        # gets the value in the array that is a division of whatever the size is
        size /=multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)
    
    raise ValueError('That Number is too Large')

if __name__ == '__main__':
    print(approx_size(1000000000000, False))
    print(approx_size(1000000000000))
    print(approx_size(1000, False))
    print(approx_size(1000))
    print(approx_size(100000, False))
    print(approx_size(100000))

