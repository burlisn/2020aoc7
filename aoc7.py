def main() -> None:
    #open input text file and get input
    with open("input.txt", "r") as fin:
        inputText=fin.read()

    #obtain list of bagNames
    inputList=inputText.split()
    bagList=[]
    for i,word in enumerate(inputList):
        if "bag" in word and inputList[i-3] != 'contain':
            if inputList[i-2]+' '+inputList[i-1] not in bagList:
                bagList.append(inputList[i-2]+' '+inputList[i-1])

    #Create dictionary of which bags that bag is contained in
    bagHier={bags: [] for bags in bagList}
    bagHier2={bags: [] for bags in bagList}
    inputLines=inputText.split('\n')
    for i,line in enumerate(inputLines):
        lineWords=line.split()
        bagType=lineWords[0]+' '+lineWords[1]
        
        for bags in bagList:
            if bags in line and bags != bagType:
                bagHier[bags].append(bagType)
                bagHier2[bagType].append((bags, line[line.index(bags)-2]))
    
    #Create a list of colors that can eventually hold the shiny gold bag
    canHold=[] #list of bags that hold the shiny gold bag
    the_chain(bagHier, 'shiny gold', canHold)

    #------ Part 2 ---------------
    gold_holds=0
    gold_holds=rec_gold_hold(bagHier2, gold_holds, 'shiny gold')[0]
    
    #Print answer part 1 & 2
    print(len(canHold))
    print(gold_holds)

# ------------------- functions ------------------------

#recursively adds bags that can hold the 'shiny gold' bag to the canHold list
def the_chain(bagHier: dict[str, list], bag: str, canHold: list):
    for bags in bagHier[bag]:
        if bags not in canHold:
            canHold.append(bags)
        the_chain(bagHier, bags, canHold)

#recursively counts the number of bags that the 'shiny gold' bag can hold to the goldHolds variable
def rec_gold_hold(bagHier2: dict[str, list[tuple]], goldHolds: int, bag: str):
    bags_i_contain=0
    for bags in bagHier2[bag]: #for the bags I hold
        bags_i_contain+=int(bags[1])*rec_gold_hold(bagHier2, goldHolds, bags[0])[1]+int(bags[1])
    goldHolds+=bags_i_contain
    return (goldHolds, bags_i_contain)
        
        
if __name__ == "__main__":
    main()
