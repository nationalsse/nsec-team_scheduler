num_teams = int(raw_input("Number of teams competing: "))
num_rounds = int(raw_input("Number of rounds: "))
num_judge_slots = int(raw_input("Number of judges per round: "))

print "Scheduling " + str(num_teams) + " teams for " + str(num_rounds) + " rounds with " + str(num_judge_slots) + " judges per round"

# Create an n by n array where n is the number of teams
comparison_matrix = [["" for i in range(num_teams)] for j in range(num_teams)]

schedule = [[0 for i in range(num_judge_slots)] for j in range(num_teams)]

def initMatrix():
    for i in range(len(comparison_matrix)):
        for j in range(len(comparison_matrix[i])):
            if(i == j): comparison_matrix[i][j] = "-"
    
    for i in range(len(comparison_matrix)):
        j = 0
        while (comparison_matrix[i][j] != "-"):
            comparison_matrix[i][j] = "x"
            j = j + 1
            

def printMatrix():
    for i in range(len(comparison_matrix)):
        for j in range(len(comparison_matrix[i])):
            print str(comparison_matrix[i][j]) + " ",
        print "\n",
    print "---------------------"

def updateMatrix(team1, team2):
    comparison_matrix[team1][team2] = "x"
    comparison_matrix[team2][team1] = "x"

def checkMatrix(team1, team2):
    print "Hi"

def scheduleTeams():
    currentTeam = 0
    currentTeamOpponent = 0
    alreadyUsedThisRound = []

    for i in range(num_teams):
        currentTeam = i
        if currentTeam in alreadyUsedThisRound:
            continue
        for j in range(num_teams):
            currentTeamOpponent = j
            if j == "-" or j == "x" or currentTeamOpponent in alreadyUsedThisRound:
                continue
            alreadyUsedThisRound.append(currentTeam)
            alreadyUsedThisRound.append(currentTeamOpponent)
            updateMatrix(currentTeam, currentTeamOpponent)
    
scheduleTeams()
printMatrix()