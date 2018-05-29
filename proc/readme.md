脚本功能：
    根据配置拷贝文件，详细查看配置项注释

启动：
    python prefile.py _arg &

杀进程：
    ps aux|grep python|awk '{if($12 == "prefile.py" && $13 == "_arg") print $2}' | xargs kill -9

杀进程2：
    需要stop.py脚本，参数为prefile.py对应的输入参数(标签)
    python stop.py _arg

查看日志：
    tail -99f _arg.log

_arg 对应.cfg配置文件的标签



