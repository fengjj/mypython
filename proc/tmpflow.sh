#tmpflow.sh

dir=$1
num=$2

start_hour=`echo $dir|awk -F  "/" '{print $NF}'`   
if [ "$start_hour" == "" ];then
    start_hour=`echo $dir|awk -F  "/" '{print $(NF-1)}'`   
fi



echo $start_hour
day_hour=$start_hour
current_hour=`date +'%Y%m%d%H' `
echo 
cd /data/proc
while(( $day_hour <= current_hour ))
do  
    new_dir=` echo $dir | sed "s/${start_hour}/${day_hour}/" `
    nohup python tmpflow.py $new_dir $num >/data/proc/log/flow${day_hour}_${num}.log  &
    start_day=`echo $day_hour | cut -c 1-8`
    hour=`echo $day_hour | cut -c 9-10`
    echo $start_day  $hour
    day_hour=`date -d "$start_day $hour 1 hour" +"%Y%m%d%H"`
    echo $day_hour
    
done

