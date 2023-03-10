# 自定义Logger类用来快速创建日志器
import logging
import sys

class Logger(object):

    LOGGER_NAME = "MayaLogger"

    LEVEL_DEFAULT = logging.DEBUG
    PROPAGATE_DEFAULT = False

    _logger_obj = None


    @classmethod
    def logger_obj(cls):

        if not cls._logger_obj:
            if cls.logger_exists():
                cls._logger_obj = logging.getLogger(cls.LOGGER_NAME)
            else:
                cls._logger_obj = logging.getLogger(cls.LOGGER_NAME)

                cls._logger_obj.setLevel(cls.LEVEL_DEFAULT)
                cls._logger_obj.propagate = cls.PROPAGATE_DEFAULT

                fmt = logging.Formatter("[%(levelname)s][%(name)s] %(message)s")

                stream_handler = logging.StreamHandler(sys.stdout)
                stream_handler.setFormatter(fmt)
                cls._logger_obj.addHandler(stream_handler)
        
        return cls._logger_obj
    
    @classmethod
    def logger_exists(cls):
        return cls.LOGGER_NAME in logging.Logger.manager.loggerDict.keys()
    
    @classmethod
    def set_level(cls, level):
        lg = cls.logger_obj()
        lg.setLevel(level)
    
    @classmethod
    def set_propagate(cls, propagate):
        lg = cls.logger_obj()
        lg.propagate = propagate

    @classmethod
    def debug(cls, msg, *args, **kwargs):
        lg = cls.logger_obj()
        lg.debug(msg,*args, **kwargs)

    @classmethod
    def info(cls, msg, *args, **kwargs):
        lg = cls.logger_obj()
        lg.info(msg,*args, **kwargs)
    
    @classmethod
    def warning(cls, msg, *args, **kwargs):
        lg = cls.logger_obj()
        lg.warning(msg,*args, **kwargs)
    
    @classmethod
    def error(cls, msg, *args, **kwargs):
        lg = cls.logger_obj()
        lg.error(msg,*args, **kwargs)
    
    @classmethod
    def critical(cls, msg, *args, **kwargs):
        lg = cls.logger_obj()
        lg.critical(msg,*args, **kwargs)
    
    @classmethod
    def log(cls, msg, *args, **kwargs):
        """ 自定义等级的日志信息 """
        lg = cls.logger_obj()
        lg.log(msg,*args, **kwargs)
    
    @classmethod
    def exception(cls, msg, *args, **kwargs):
        """ 针对异常处理的日志信息 """
        lg = cls.logger_obj()
        lg.exception(msg,*args, **kwargs)

    @classmethod
    def write_to_file(cls, path, level=logging.WARNING):
        file_handler = logging.FileHandler(path)
        file_handler.setLevel(level)

        fmt = logging.Formatter("[%(asctime)s][%(levelname)s] %(message)s")
        file_handler.setFormatter(fmt)

        lg = cls.logger_obj()
        lg.addHandler(file_handler)

    
if __name__ == "__main__":

    # Logger.set_level(logging.WARNING)

    # Logger.write_to_file("C:/Users/Administrator/Desktop/test.log")

    Logger.set_propagate(False)

    Logger.debug("debug message")
    Logger.info("info message")
    Logger.warning("warning message")
    Logger.error("error message")
    Logger.critical("critical message")
    # Logger.log(5, "log message")

    # try:
    #     a = []
    #     b = a[0]
    # except:
    #     Logger.exception("exception message")