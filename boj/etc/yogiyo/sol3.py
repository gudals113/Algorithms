from typing import List, Text


class NoAgentFoundException(Exception):
    pass


class Agent(object):
    def __init__(self, name, skills, load):
        self.name = name
        self.skills = skills
        self.load = load
        
    def __str__(self):
        return "<Agent: {}>".format(self.name)


class Ticket(object):
    def __init__(self,id, restrictions):
        self.id = id
        self.restrictions = restrictions
        


class FinderPolicy(object):
    def _filter_loaded_agents(self, agents: List[Agent]) -> List[Agent]:
        tmp = []
        for agent in agents :
            if agent.load <3 :
                tmp.append(agent)
        return tmp

    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        sol =None
        agents = self._filter_loaded_agents(agents)
        least_loaded_policy = LeastLoadedAgent()
        least_flexible_policy = LeastFlexibleAgent()
        flex_sort = least_flexible_policy.find(ticket, agents)
        sol=least_loaded_policy.find(ticket, flex_sort)
        
        if sol == None :
            raise NoAgentFoundException
        elif sol.load>=3:
            raise NoAgentFoundException
        else:
            return(sol)


class LeastLoadedAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        tmp = 999
        sol = None
        for agent in agents :
            if agent.load < tmp :
                tmp = agent.load
                sol = agent

        if sol == None :
            raise NoAgentFoundException
        
        elif sol.load>=3:
            raise NoAgentFoundException
        
        else:
            return(sol)
    

class LeastFlexibleAgent(FinderPolicy):
    def find(self, ticket: Ticket, agents: List[Agent]) -> Agent:
        restrictions = ticket.restrictions
        set_restrictions = set(restrictions)
        tmp = 999
        sol = None
        for agent in agents: 
            skills = agent.skills
            set_skills = set(skills)
            length_skills = len(skills)
            if set_restrictions & set_skills == set_restrictions and length_skills<tmp:
                tmp = length_skills
                sol = agent
        
        if sol == None :
            raise NoAgentFoundException
        elif sol.load>=3:
            raise NoAgentFoundException
        else:
            return(sol)
ticket = Ticket(id="1", restrictions=["English"])
agent1 = Agent(name="A", skills=["English"], load=2)
agent2 = Agent(name="B", skills=["English", "Japanese"], load=0)

least_loaded_policy = FinderPolicy()
# returns the Agent with name "B" because of their currently lower load.
sol1 = least_loaded_policy._filter_loaded_agents([agent1, agent2])
# print(sol1)
solsol = least_loaded_policy.find(ticket, [agent1, agent2])
print(solsol)



least_loaded_policy = LeastLoadedAgent()
# returns the Agent with name "B" because of their currently lower load.
sol2= least_loaded_policy.find(ticket, [agent1, agent2])


least_flexible_policy = LeastFlexibleAgent()
# returns the Agent with name "A" because of their lower flexibility.
sol3 = least_flexible_policy.find(ticket, [agent1, agent2])
