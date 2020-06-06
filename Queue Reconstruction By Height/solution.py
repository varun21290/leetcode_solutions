class Solution:
    def reconstructQueue(self, people: [[int]]) -> [[int]]:
        people=sorted(people,key=lambda x: x[0])
        sorted_people=[[-1,-1] for _ in range(len(people))]
        for x in people:
            i=x[1]
            j=0
            while i>0 or sorted_people[j][0]!=-1:
                if sorted_people[j][0]==-1 or sorted_people[j][0]==x[0]:
                    i-=1
                j+=1
                    
            sorted_people[j]=x
            
        return sorted_people
            
    def reconstructQueueBetter(self, people: [[int]]) -> [[int]]:
        people.sort(key = lambda person: (person[0], -person[1]))
        people.reverse()
        queue = []
        for person in people:
            queue.insert(person[1],person)
        return queue
