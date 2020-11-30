# Week 4 Task

def readFastq(file_name):
    sequences = []
    qualities = []
    with open(file_name) as fq:
        while True:
            fq.readline()
            read = fq.readline().strip()
            fq.readline()
            ql = fq.readline().strip()
            if len(read) == 0:
                break
            sequences.append(read)
            qualities.append(ql)
    return sequences, qualities

def readFasta(file_name):
    sequences = []
    with open(file_name) as fa:
        while True:
            read = fa.readline().strip()
            if len(read) == 0:
                break
            if read[0] == '>':
                continue
            sequences.append(read)
    return sequences



# Main function to use in reading fasta or fastq files.

def readFile(file_name):
    fileID = ''
    with open(file_name) as fl:
        fileID = fl.readline()[0]
    if fileID == '@':
        return readFastq(file_name)
    elif fileID == '>':
        return readFasta(file_name)
    else:
        return -1


def Phred33_to_Q(qual):
    return ord(qual) - 33

def Q_to_Phred33(qual):
    return chr(qual+33)


sq,q = readFile('sample.fastq')
print(sq[:2])
print(q[:2])

sa = readFile('ecoli_rel606.fasta')
print(sa[:2])

print(Phred33_to_Q('H'))
print(Q_to_Phred33(35))
