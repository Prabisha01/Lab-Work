#you live 4 miles from the university. The bus drives at 25mph but spends 2 minutes at each
#10 stops on the the way. How long will the bus journey take?
#You jog first mile at 7 mph; then run next two at 15 mph
#jogging the last at 7mph again. will this be quiker or slower than bus?

stoppedtime=2*10
distance=4
speedMph= 25/60
drivingtime= distance/speedMph
totaltimebybus=drivingtime+stoppedtime
runningtime=((1/7)+(2/15)+(1/7))*60
print(f"the total time taken by the bus is {totaltimebybus}")
print(f"the total time taken while jogging is {runningtime}")
if totaltimebybus>runningtime:
    print("Bus takes more time than jog")
else:
    print("bus takes less time than jog")