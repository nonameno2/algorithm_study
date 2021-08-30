# https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    
    answer = 0                                              # the time it takes for all trucks to cross the bridge, zero initialization
    w = 0                                                   # the weight of the truck crossing the bridge, zero initialization
    q = deque(truck_weights)                                # waiting truck queue 
    bridge = deque([0 for _ in range(bridge_length)])       # bridge queue  
    
    while q or w > 0:                                       # while there is truck in the queue or truck on the bridge

        removed_truck = bridge.popleft()                    # pop truck that has already crossed the bridge
        w -= removed_truck                                  # subtract weight
        
        if q and w + q[0] <= weight:                        # conditions under which the next truck can cross the bridge
            new_truck = q.popleft()                         # pop the element from the queue q
            w += new_truck                                  # add weight
            bridge.append(new_truck)                        # push the element to the queue bridge 
        else:                                               # if the new truck can't get on the bridge
            bridge.append(0)                                # fill with zero

        answer += 1                                         # add time

    
    return answer
