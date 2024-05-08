import sys
from pyke import knowledge_engine, krb_traceback

engine = knowledge_engine.engine(__file__)

def fc_rules_fn():
  engine.reset()
  engine.activate("fc_rules")

  try:
    # with engine.prove_goal("facts.has_depression($name_patient, $status)") as gen:
    #   for vars, plan in gen:
    #     name_patient = vars['name_patient']
    #     status = vars['status']
    #     print("Dear", name_patient, "-", status)

    with engine.prove_goal("facts.recommendation_message($name_patient, $message)") as gen:
      for vars, plan in gen:
        name_patient = vars['name_patient']
        message = vars['message']
        print("Dear", name_patient, "-", message)
  except Exception as e:
    print("Error:", e)
    krb_traceback.print_exc()
    sys.exit(1)

def fc_questions_fn():
  engine.reset()
  engine.activate("fc_questions_rules")

  try:
    # with engine.prove_goal("facts.depression_severity($total_score, $severity)") as gen:
    #   for vars, plan in gen:
    #     name_patient = vars['total_score']
    #     total_score = vars['severity']
    #     print("Dear", name_patient, "-", total_score)

    with engine.prove_goal("facts.recommendation_message($name_patient, $message)") as gen:
      for vars, plan in gen:
        print("Dear %s," % vars['name_patient'].capitalize())
        print(vars['message'])
  except Exception as e:
    print("Error:", e)
    krb_traceback.print_exc()
    sys.exit(1)

if __name__ == "__main__":
  # fc_rules_fn()
  fc_questions_fn()