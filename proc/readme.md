�ű����ܣ�
    �������ÿ����ļ�����ϸ�鿴������ע��

������
    python prefile.py _arg &

ɱ���̣�
    ps aux|grep python|awk '{if($12 == "prefile.py" && $13 == "_arg") print $2}' | xargs kill -9

ɱ����2��
    ��Ҫstop.py�ű�������Ϊprefile.py��Ӧ���������(��ǩ)
    python stop.py _arg

�鿴��־��
    tail -99f _arg.log

_arg ��Ӧ.cfg�����ļ��ı�ǩ



