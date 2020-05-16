
#open file

def loadData():
    year = 1928
    infile = open("oscars.txt")
    table = []
    for line in infile.readlines():
        data = line.strip().split(',')
        table.append(data)
    for row in table:
        row.append(year)
        year+=1

    return table

def outputTable(table):
    print("Oscar winning genres are:\n")
    count=0
    strformat = "{0:20s}"
    genres = []


    for row in table:
        row = row[1]

        if row not in genres:
            genres.append(row)
    #print(genres)
    for i in genres:
        print(strformat.format(i),end="")
        count += 1
        if count%5 == 0:
            print()

def main():
    oscar_data = loadData()
    print(oscar_data)
    done = False
    #while not done:
    outputTable(oscar_data)
    genre = input("\n\nEnter a genre: ")
    print(f"The Academy Award winners for Best Picture in the {genre} genre are:\n")

    for row in oscar_data:
        if row[1] == genre.lower():
             if genre in row:
                 print(f"\t{row[0]}")
    year = int(input("\nEnter year in between 1928 and 1953: "))
    for row in oscar_data:
        if row[2] == year:
            print(f"\nBest Film: {row[0]}")
            print(f"\nGenre: {row[1]}")
        
               


main()
