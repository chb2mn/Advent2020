
card_subject_number = 7
door_subject_number = 7

def handshake(subject_number, loop_size):
    value = 1
    for i in range(loop_size):
        value *= subject_number
        value = value % 20201227
    return value

def find_loop_size(subject_number, public_key):
    value = 1
    i=0
    while value != public_key:
        value *= subject_number
        value = value % 20201227
        i+=1
    return i

if __name__ =='__main__':
    with open('input.txt', 'r') as fin:
        card_public_key = int(fin.readline().strip())
        door_public_key = int(fin.readline().strip())
    #first find the loop size by brute force 
    card_loop_size = find_loop_size(card_subject_number, card_public_key)
    door_loop_size = find_loop_size(door_subject_number, door_public_key)
    print(card_loop_size)
    print(door_loop_size)
    print("enc key:")
    print(handshake(card_public_key, door_loop_size))
    print(handshake(door_public_key, card_loop_size))
