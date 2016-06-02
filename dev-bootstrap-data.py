import os
from django.core.wsgi import get_wsgi_application
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "desaga.settings")
application = get_wsgi_application()

from datetime import datetime, date, timedelta
from registrar.models import *

def get_demo_lab():
    labs = Lab.objects.filter(name='demo')
    if len(labs) == 1:
        return labs[0]
    else:
        lab_type = LabType(name='docker', display_name='Docker Based Lab', 
                           implementation_class='some.package.Docker')
        lab_type.save()
        
        lt_metaparam = LabTypeMetaparameter(lab_type=lab_type,
                                            name='image',
                                            display_name='Image Source',
                                            description='Image Source',
                                            parameter_type='STR',
                                        )
        lt_metaparam.save()
        
        lab = Lab(name='demo', slug='demo', maximum_students=20, start_date=datetime.now(),
                  lab_type=lab_type)
        lab.save()
        return lab
        
if __name__ == '__main__':
    lab = get_demo_lab()
    tim = User.objects.filter(username='tim')[0]

    ssh_key = SSHKey(user=tim, name='euclid', public_key='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDS3wsMYZYcRubjc2XU/XNH/fxdYOfcNmzsl1daVTAy1D3boxhVdSPCMYBSzmIR51t9RL6tq+Dpseyyn1MhoxCXEAbF0UnhkpZ1OKoxjOpOHQwmgdXykvfiAAsGfOhpUOqvOxWJcYdPsyj4ofqODoJofVxNboBndo5/Tw+Wr6HGWSisEv77JLEv5KWA2AGQXG4SvgGzK/GWQiLdIRquBILSXFV7TdTEMi5OuLanC5+S3u2RFaZBSdfOlDnjFAOZgbrggULHdAXN0oaR0n3Pvm8w3TlaOR4oOQV14d9H+vfgzYeGXj31kTVCLaK1hR3ORmeUzNvVdIVi7vg20nMu5K+JyCcqK12vIF9Aa3uE8sVVROEpWxIYtlbE47ZHmSg7clgnW3vjVSWQiyFQ4Z4la5mkLscpAGSnkd525/EiibJyfLKjLd+i5a9aQjoOoUlhcItrqHs9m70tgqMSGkqA8xreZOCFKokG7yDD9FQL0h5HtF2ilIIPABAHfLFQwsinwkpMz2IASS/SrHp3hUAXwX3wknsoAAOvoGQvtoLDXkRSJqAclXzGBZDvQwR5nlqSguM/2LKwPig8U13onnH37oCxhux6uJL/fygoUzdl8VooM4Q46GgJwBZXuC6JA+89LJX5Gx5TTsWDmRBWL5MRVavd0jwgdvA66VXpsO0Zqw9N+Q== tim@euclid')
    ssh_key.save()

    staff_reg = StaffRegistration(user=tim, lab=lab)
    staff_reg.save()

    student_reg = StudentRegistration(user=tim, lab=lab)


