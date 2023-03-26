def main():
    noun = input('noun: ')
    verb = input('verb: ')
    adj = input('adj: ')
    adverb = input('adverb: ')
    interpolation = interpolation_string(noun,verb,adj,adverb)
    print(interpolation)


def interpolation_string(n,v,adj,adv):
    return f'Does the {adj} {n} {v} {adv}? That is insane.'




if __name__ == '__main__':
    main()
