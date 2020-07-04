# -*- encoding:utf-8 -*-
# __Author__:yuslience
import sys
import os
import logbook
import logbook.more


def log_layout(record, handler):
    _log_layout = "[{date}] [{level}] [{filename}] {msg}".format(
        date=record.time,         # 日志时间
        level=record.level_name,  # 日志等级
        filename=os.path.split(record.filename)[-1],  # 文件名
        # func_name=record.func_name,  # 函数名
        # lineno=record.lineno,        # 行号
        msg=record.message             # 日志内容
    )
    return _log_layout


def init_logger(filename, file_log_flag=True, std_out_flag=False):
    log_dir = os.path.join('log')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logbook.set_datetime_format('local')
    logger = logbook.Logger(filename)
    logger.handlers = []
    if file_log_flag:  # 日志输出到文件
        log_file = logbook.TimedRotatingFileHandler(os.path.join(log_dir, '%s.log' % filename),
                                                    date_format='%Y-%m-%d',
                                                    rollover_format='{basename}{ext}.{timestamp}',
                                                    backup_count=14,
                                                    bubble=True,
                                                    encoding='utf-8')
        log_file.formatter = log_layout
        logger.handlers.append(log_file)

    if std_out_flag:  # 日志打印到屏幕
        log_std = logbook.more.ColorizedStderrHandler(bubble=True)
        log_std.formatter = log_layout
        logger.handlers.append(log_std)
    return logger


def get_share_logger(_file_name):
    return init_logger(_file_name, True, True)


def set_share_logger(logger):
    init_logger('log.txt', True, True).logger = logger
