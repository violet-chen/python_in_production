import logging
import sys

logger_obj = logging.getLogger("RuiChen") # 创建日志器
logger_obj.setLevel(logging.DEBUG) # 设置等级

fmt = logging.Formatter("[%(name)s][%(levelname)s] %(message)s") # 创建格式器

handler = logging.StreamHandler(sys.stderr) # 创建处理器决定日志输出的地方
handler.setFormatter(fmt)
logger_obj.addHandler(handler)
# 输出不同等级的信息
logger_obj.critical("critical message")
logger_obj.error("error message")
logger_obj.warning("warning message")
logger_obj.info("info message")
logger_obj.debug("debug message")