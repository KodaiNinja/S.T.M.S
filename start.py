o
    U�Dc�  �                   @   sd  d dl Z d dlZd dlZd dlZd dlZe�d� d dlZej�ejd  d�Z	e�
� Ze�e	� e�dd�Zedkr_e�d� ded d< edd��Ze�e� W d  � n1 sZw   Y  d d	lmZmZmZmZ d d
lmZ d dlmZ d dlmZmZ e�  dd� Zdd� Zdd� Zdd� Zdd� Z e!dkr�edkr�e j"j#�$d� e�%� �&e d�� dS dS )�    Nzpip install configparserzcore\config.ini�configZfirst_setupZyesz,pip install colorama && pip install telethon�w)�init�Fore�Style�Back)�platform)�TelegramClient)�	functions�typesc                   C   s�   t tjd � t tjd � t tjd � t tjd � t tjd � t tjd � t tjd � t tjtj d tj � d S )	Nu<   ╔═══╦════╦═╗╔═╗╔═══╗u8   ║╔═╗║╔╗╔╗║ ╚╝ ║║╔═╗║u<   ║╚══╬╝║║╚╣╔╗╔╗║║╚══╗u8   ╚══╗║ ║║ ║║║║║║╚══╗║u<   ║╚═╝╠╗║║╔╣║║║║╠╣╚═╝║u<   ╚═══╩╝╚╝╚╩╝╚╝╚╩╩═══╝z"Simple telegram marketing softwarezTRIAL VERSION)�printr   �RED�WHITEr   r   Z	RESET_ALL� r   r   �start.py�logo   s   r   c                  �   sd   �t dkrt�d� nt�d� td�} | dkrt��  d S | dkr*t� I d H  d S t� I d H  d S )N�win32�cls�clear�Exit? y/n
 > �y�n)r   �os�system�input�abort�main�ext)�answerr   r   r   r   (   s   �
r   c                 �   s�   �t dkrt�d� nt�d� z	| �� I d H  W n   Y td�}|dkr,t��  d S |dkr9td�I d H  d S t| �I d H  d S )Nr   r   r   r   r   r   � )r   r   r   �
disconnectr   r   r   �ext2��clientr   r   r   r   r!   6   s   �
r!   c               
   �   sz  �t dkrt�d� nt�d� g } tdddd��}|D ]}| �|�dd	�� qW d   � n1 s2w   Y  t�| �}td
t	|�
d�d �||�d�d d � �}|�� I d H  |�� I d H  ttjd � ttjd � ttjd � ttjd � ttjd � ttjtj d tj �}|dkr�t|�I d H  d S |dk�r�t	ttjtj d ��}g }tdddd��}|D ]}|�|�dd	�� q�W d   � n1 s�w   Y  ttjtj d � z�tt|��D ]�}d}	t|�D ]�}
|	d7 }	zH|tjj|| t�� dd��I d H  t dk�rtj j!�"dt#|	�� d�||  d � ttj$dt#|	�� d� tj tj ||  tj d � W q�   t dk�rXtj j!�"dt#|	�� d�||  d � ttj$dt#|	�� d� tj tj ||  tj d � Y q�q�ttjtj d � |�%� I d H  t&|�I d H  W d S    ttjd  � |�%� I d H  t&|�I d H  Y d S ttjd  � t&|�I d H  d S )!Nr   r   r   zinput\accounts.txt�r�utf8)�encoding�
r   zS.T.M.S�:r   �   um   █▀▀█ █▀▀ █▀▀█ █▀▀█ █▀▀█ ▀▀█▀▀  ▀  █▀▀▄ █▀▀▀u[   █▄▄▀ █▀▀ █  █ █  █ █▄▄▀   █   ▀█▀ █  █ █ ▀█ua   █  █ ▀▀▀ █▀▀▀ ▀▀▀▀ ▀ ▀▀   ▀   ▀▀▀ ▀  ▀ ▀▀▀▀

z
[0] - Backz[1] - Start
� > �0�1zHow many reports send: zinput\usernames_list.txtz
----STARTED----
zSPAM SPAM SPAM)Zpeer�reason�message�[z]  z	  successz  errorz
----FINISHED----
�&Check that the data entered is correct)'r   r   r   �open�append�replace�random�choicer	   �int�	partition�find�startZconnectr   r   r   r   r   ZYELLOWr   ZBRIGHTZGREENr   �range�lenr
   ZaccountZReportPeerRequestr   ZInputReportReasonSpam�ctypes�windll�kernel32�SetConsoleTitleW�strZBLUEr    r!   )Zaccounts�file�lineZaccr#   �methodZcnt�members�iZcnt2�jr   r   r   �	reportingH   s~   �
��
,
���
&0
�
&0
��rG   c                 �   s�   �t dkrt�d� nt�d� t dkrtjj�d� z	| �� I d H  W n   Y t�  t	t
jd � t	t
jd � td�}|dkrJt� I d H  d S |d	krVt� I d H  d S t	t
jd
 � t� I d H  d S )Nr   r   r   �   🚀 ∙ S.T.M.Sz

[0] - Exitz[1] - Reporting
r*   r+   r,   r0   )r   r   r   r<   r=   r>   r?   r    r   r   r   r   r   r   rG   r   r"   r   r   r   r   �   s(   �
r   �__main__r   rH   r   )'r<   r4   �sysZasyncior   r   Zconfigparser�path�joinZconfig_pathZConfigParserr   �read�getZansr1   Z
configfile�writeZcoloramar   r   r   r   r   Ztelethonr	   r
   r   r   r   r!   rG   r   �__name__r=   r>   r?   Zget_event_loopZrun_until_completer   r   r   r   �<module>   s@    


�K �