o
    UDc  γ                   @   sd  d dl Z d dlZd dlZd dlZd dlZe d‘ d dlZej ejd  d‘Z	e 
‘ Ze e	‘ e dd‘Zedkr_e d‘ ded d< eddZe e‘ W d   n1 sZw   Y  d d	lmZmZmZmZ d d
lmZ d dlmZ d dlmZmZ e  dd Zdd Zdd Zdd Zdd Z e!dkr°edkr₯e j"j# $d‘ e %‘  &e d‘ dS dS )ι    Nzpip install configparserzcore\config.iniΪconfigZfirst_setupZyesz,pip install colorama && pip install telethonΪw)ΪinitΪForeΪStyleΪBack)Ϊplatform)ΪTelegramClient)Ϊ	functionsΪtypesc                   C   s   t tjd  t tjd  t tjd  t tjd  t tjd  t tjd  t tjd  t tjtj d tj  d S )	Nu<   βββββ¦βββββ¦ββββββββββu8   ββββββββββ ββ ββββββu<   βββββ¬βββββ£ββββββββββu8   βββββ ββ βββββββββββu<   βββββ βββββ£βββββ β£ββββu<   βββββ©βββββ©βββββ©β©ββββz"Simple telegram marketing softwarezTRIAL VERSION)Ϊprintr   ΪREDΪWHITEr   r   Z	RESET_ALL© r   r   ϊstart.pyΪlogo   s   r   c                  Γ   sd   t dkrt d‘ nt d‘ td} | dkrt ‘  d S | dkr*t I d H  d S t I d H  d S )NΪwin32ΪclsΪclearϊExit? y/n
 > ΪyΪn)r   ΪosΪsystemΪinputΪabortΪmainΪext)Ϊanswerr   r   r   r   (   s   
r   c                 Γ   s   t dkrt d‘ nt d‘ z	|  ‘ I d H  W n   Y td}|dkr,t ‘  d S |dkr9tdI d H  d S t| I d H  d S )Nr   r   r   r   r   r   Ϊ )r   r   r   Ϊ
disconnectr   r   r   Ϊext2©Ϊclientr   r   r   r   r!   6   s   
r!   c               
   Γ   sz  t dkrt d‘ nt d‘ g } tdddd}|D ]}|  | dd	‘‘ qW d    n1 s2w   Y  t | ‘}td
t	| 
d‘d || d‘d d  }| ‘ I d H  | ‘ I d H  ttjd  ttjd  ttjd  ttjd  ttjd  ttjtj d tj }|dkrt|I d H  d S |dkr­t	ttjtj d }g }tdddd}|D ]}| | dd	‘‘ qΊW d    n1 sΠw   Y  ttjtj d  z²tt|D ]}d}	t|D ]}
|	d7 }	zH|tjj|| t ‘ ddI d H  t dkrtj j! "dt#|	 d||  d ‘ ttj$dt#|	 d tj tj ||  tj d  W qξ   t dkrXtj j! "dt#|	 d||  d ‘ ttj$dt#|	 d tj tj ||  tj d  Y qξqζttjtj d  | %‘ I d H  t&|I d H  W d S    ttjd   | %‘ I d H  t&|I d H  Y d S ttjd   t&|I d H  d S )!Nr   r   r   zinput\accounts.txtΪrΪutf8)ΪencodingΪ
r   zS.T.M.Sϊ:r   ι   um   ββββ βββ ββββ ββββ ββββ βββββ  β  ββββ ββββu[   ββββ βββ β  β β  β ββββ   β   βββ β  β β ββua   β  β βββ ββββ ββββ β ββ   β   βββ β  β ββββ

z
[0] - Backz[1] - Start
ϊ > Ϊ0Ϊ1zHow many reports send: zinput\usernames_list.txtz
----STARTED----
zSPAM SPAM SPAM)ZpeerΪreasonΪmessageϊ[z]  z	  successz  errorz
----FINISHED----
ϊ&Check that the data entered is correct)'r   r   r   ΪopenΪappendΪreplaceΪrandomΪchoicer	   ΪintΪ	partitionΪfindΪstartZconnectr   r   r   r   r   ZYELLOWr   ZBRIGHTZGREENr   ΪrangeΪlenr
   ZaccountZReportPeerRequestr   ZInputReportReasonSpamΪctypesΪwindllΪkernel32ΪSetConsoleTitleWΪstrZBLUEr    r!   )ZaccountsΪfileΪlineZaccr#   ΪmethodZcntΪmembersΪiZcnt2Ϊjr   r   r   Ϊ	reportingH   s~   
??
,
??ύ
&0
?
&0
?ρrG   c                 Γ   sΚ   t dkrt d‘ nt d‘ t dkrtjj d‘ z	|  ‘ I d H  W n   Y t  t	t
jd  t	t
jd  td}|dkrJt I d H  d S |d	krVt I d H  d S t	t
jd
  t I d H  d S )Nr   r   r   υ   π β S.T.M.Sz

[0] - Exitz[1] - Reporting
r*   r+   r,   r0   )r   r   r   r<   r=   r>   r?   r    r   r   r   r   r   r   rG   r   r"   r   r   r   r      s(   
r   Ϊ__main__r   rH   r   )'r<   r4   ΪsysZasyncior   r   ZconfigparserΪpathΪjoinZconfig_pathZConfigParserr   ΪreadΪgetZansr1   Z
configfileΪwriteZcoloramar   r   r   r   r   Ztelethonr	   r
   r   r   r   r!   rG   r   Ϊ__name__r=   r>   r?   Zget_event_loopZrun_until_completer   r   r   r   Ϊ<module>   s@    


?K ύ