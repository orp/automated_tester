import sys
import os
import importlib
import importlib.util
import logging
from config import *

class StreamToLogger(object):
   """
   Fake file-like stream object that redirects writes to a logger instance.
   """
   def __init__(self, logger, log_level=logging.INFO):
      self.logger = logger
      self.log_level = log_level
      self.linebuf = ''

   def write(self, buf):
      for line in buf.rstrip().splitlines():
         self.logger.log(self.log_level, line.rstrip())
    
   def flush(self):
       pass      

def reload_modules_in_path(path):
    assert (path in sys.path)
    modules = [f.strip(".py") for f in os.listdir(path) if f.endswith(".py")]
    for mod_name in modules:
        mod = importlib.import_module(mod_name)
        importlib.reload(mod)

def grade(result, default_penalty, penalties):
    logging.debug("grading %s, %s, %s)" % (result, default_penalty, penalties))
    score = 100
    for failure in result.failures:
        test_id = failure[0].id().split(".")[-1] #the id is of form package.module.method. We want the method only
        logging.debug("failed: %s, %s" % (failure, test_id))
        if test_id in penalties:
            score -= penalties[test_id]
        else:
            score -= default_penalty
    for error in result.errors:
        test_id = error[0].id().split(".")[-1]
        if test_id in penalties:
            score -= penalties[test_id]
        else:
            score -= default_penalty
    return score
 
def log_failures(results):
    for failure in results.failures:
        failure_instance = failure[0]
        test_id = failure_instance.id().split(".")[-1]
        test_method = getattr(failure_instance, test_id)
        failure_info = test_method.__doc__ if test_method.__doc__ is not None else test_method.__name__
        logging.info("Failed test description: %s)" % failure_info)
        
                
def run_test_module(test_module_name, test_module_path, solution_script_path):
    """Runs a test suite for a module. The function expects a test module name and path (that conforms to the unittest protocol) as well as the path
    to the solution code and an open log file
    for example, if the test code is in module test_foo.py in path /foo_tester and the solution code is in /solutions/foo.py then run the function with
    run_test_module(test_foo, /foo_tester, /solutions, log_file)"""
    logging.debug("running test module for solution path %s" % solution_script_path)
    temp_sys_path = sys.path[:]
    sys.path.append(solution_script_path)
    sys.path.append(test_module_path)
    reload_modules_in_path(solution_script_path)
    test_mod = importlib.import_module(test_module_name)
    test_mod = importlib.reload(test_mod)
    results = test_mod.run_tests()
    log_failures(results)
    score = grade(results, test_mod.default_penalty, test_mod.penalties)
    logging.info("final score for %s is %s" % (solution_script_path, score))
    sys.path = temp_sys_path

def check_solutions(solution_root_path, test_module_name, test_module_path):
    """this function checks all the solutions for a given exercise.
    The assumption is that all the solutions are in individual sub directories of the solution root directory    
    The results and the scoring are logged to the solution root directory"""
    dir_name, sub_dir_list, file_list = next(os.walk(solution_root_path))
    for solution_dir in sub_dir_list: 
         logging.info("running solution in directory %s" % solution_dir)
         run_test_module(test_module_name, test_module_path, os.path.join(dir_name, solution_dir))
         logging.info("completed execution of solution in directory %s" % solution_dir)
    
if __name__ == "__main__":
    logging.basicConfig(
        filename=os.path.join(solution_root, "test_results.txt"),
        level=logging.DEBUG, 
        filemode='w')
    stdout_logger = logging.getLogger('STDOUT')
    sl = StreamToLogger(stdout_logger, logging.INFO)
    #~ sys.stdout = sl
    
    stderr_logger = logging.getLogger('STDERR')
    sl = StreamToLogger(stderr_logger, logging.ERROR)
    #~ sys.stderr = sl

    logging.info("@@@starting_test@@@")
    check_solutions(solution_root, mod_name, mod_path)
    logging.info("@@@finished_test@@@")
    


