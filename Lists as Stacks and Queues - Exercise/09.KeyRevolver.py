from collections import deque

pricePerBullet = int(input())
sizeOfGunBarrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
money = int(input())

priceOfWholeBullets = pricePerBullet * len(bullets)
money -= priceOfWholeBullets

saveBarrel = sizeOfGunBarrel

while(bullets and locks):
    currentBullet = bullets.pop()

    if(currentBullet <= locks[0]):
        print("Bang!")
        saveBarrel -= 1
        locks.popleft()
    elif(currentBullet > locks[0]):
        print("Ping!")
        saveBarrel -= 1

    if(saveBarrel == 0 and bullets):
        saveBarrel = sizeOfGunBarrel
        print("Reloading!")

money += pricePerBullet * len(bullets)

if (not locks):
    print(f"{len(bullets)} bullets left. Earned ${money}")

else:
    print(f"Couldn't get through. Locks left: {len(locks)}")