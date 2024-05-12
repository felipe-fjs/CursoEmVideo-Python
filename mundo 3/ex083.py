exp = str(input('Digite uma expreção matética: ')).strip()
        parent = []
        parent1 = []
        parent2 = []
        for c in range(len(exp)):
            if exp[c] in ['(', ')']:
                parent.append(exp[c])
        if len(parent) % 2 == 0:
            for c in range(len(parent)):
                if parent[c] == '(':
                    parent1.append(parent[c])
                else:
                    parent2.append(parent[c])
        else:
            parent1 = 1
            parent2 = 0

        chave = []
        chave1 = []
        chave2 = []
        for c in range(len(exp)):
            if exp[c] in ['{', '}']:
                chave.append(exp[c])
        if len(chave) % 2 == 0:
            for c in range(len(parent)):
                if parent[c] == '{':
                    chave1.append(chave[c])
                else:
                    chave2.append(chave[c])
        else:
            chave1 = 1
            chave2 = 2


        col = []
        col1 = []
        col2 = []
        for c in range(len(exp)):
            if exp[c] in ['[', ']']:
                col.append(exp[c])
        if len(col) % 2 == 0:
            for c in range(len(parent)):
                if parent[c] == '[':
                    col1.append(col[c])
                else:
                    col2.append(col[c])
        else:
            col1 = 1
            col2 = 2

        if parent1 == parent2 and chave1 == chave2 and col1 == col2:
            return True
        else:
            return False
