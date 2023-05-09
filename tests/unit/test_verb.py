from boaviztapi.service.verbose import verbose_component, verbose_device


def test_verbose_component_cpu_1(complete_cpu_model):
    verbose = verbose_component(complete_cpu_model)
    assert verbose["core_units"] == {'status': 'INPUT', 'value': 24}
    assert verbose["die_size_per_core"] == {'status': 'INPUT', 'unit': 'mm2', 'value': 0.245}

    assert verbose["impacts"] == {'adp': {'description': 'Use of minerals and fossil ressources',
                                          'embedded': {'max': 0.041,
                                                       'min': 0.041,
                                                       'significant_figures': 2,
                                                       'value': 0.041},
                                          'unit': 'kgSbeq',
                                          'use': {'max': 0.00848,
                                                  'min': 4.81e-09,
                                                  'significant_figures': 3,
                                                  'value': 0.000205}},
                                  'gwp': {'description': 'Total climate change',
                                          'embedded': {'max': 43.4,
                                                       'min': 43.4,
                                                       'significant_figures': 3,
                                                       'value': 43.4},
                                          'unit': 'kgCO2eq',
                                          'use': {'max': 29000.0,
                                                  'min': 0.0084,
                                                  'significant_figures': 2,
                                                  'value': 1200.0}},
                                  'pe': {'description': 'Consumption of primary energy',
                                         'embedded': {'max': 650.0,
                                                      'min': 650.0,
                                                      'significant_figures': 3,
                                                      'value': 650.0},
                                         'unit': 'MJ',
                                         'use': {'max': 14950000.0,
                                                 'min': 0.004738,
                                                 'significant_figures': 4,
                                                 'value': 41100.0}}}


def test_verbose_component_cpu_2(incomplete_cpu_model):
    verbose = verbose_component(incomplete_cpu_model)
    assert verbose["core_units"] == {'status': 'INPUT', 'value': 12}
    assert verbose["family"] == {'status': 'INPUT', 'value': 'Skylake'}
    assert verbose["impacts"] == {'adp': {'description': 'Use of minerals and fossil ressources',
         'embedded': {'max': 0.02,
                      'min': 0.02,
                      'significant_figures': 2,
                      'value': 0.02},
         'unit': 'kgSbeq',
         'use': {'max': 0.00424,
                 'min': 2.41e-09,
                 'significant_figures': 3,
                 'value': 0.000102}},
 'gwp': {'description': 'Total climate change',
         'embedded': {'max': 19.7,
                      'min': 19.7,
                      'significant_figures': 3,
                      'value': 19.7},
         'unit': 'kgCO2eq',
         'use': {'max': 14000.0,
                 'min': 0.0042,
                 'significant_figures': 2,
                 'value': 610.0}},
 'pe': {'description': 'Consumption of primary energy',
        'embedded': {'max': 297.0,
                     'min': 297.0,
                     'significant_figures': 3,
                     'value': 297.0},
        'unit': 'MJ',
        'use': {'max': 7473000.0,
                'min': 0.002369,
                'significant_figures': 4,
                'value': 20550.0}}}


def test_verbose_component_ram(complete_ram_model):
    verbose = verbose_component(complete_ram_model)
    assert verbose["impacts"] == {'adp': {'description': 'Use of minerals and fossil ressources',
                                          'embedded': {'max': 0.034,
                                                       'min': 0.034,
                                                       'significant_figures': 2,
                                                       'value': 0.034},
                                          'unit': 'kgSbeq',
                                          'use': {'max': 0.00254,
                                                  'min': 1.44e-09,
                                                  'significant_figures': 3,
                                                  'value': 6.13e-05}},
                                  'gwp': {'description': 'Total climate change',
                                          'embedded': {'max': 530.0,
                                                       'min': 530.0,
                                                       'significant_figures': 2,
                                                       'value': 530.0},
                                          'unit': 'kgCO2eq',
                                          'use': {'max': 8600.0,
                                                  'min': 0.0025,
                                                  'significant_figures': 2,
                                                  'value': 360.0}},
                                  'pe': {'description': 'Consumption of primary energy',
                                         'embedded': {'max': 6700.0,
                                                      'min': 6700.0,
                                                      'significant_figures': 2,
                                                      'value': 6700.0},
                                         'unit': 'MJ',
                                         'use': {'max': 4472000.0,
                                                 'min': 0.001418,
                                                 'significant_figures': 4,
                                                 'value': 12300.0}}}

    assert verbose["capacity"] == {'status': 'INPUT', 'unit': 'GB', 'value': 32}
    assert verbose["density"] == {'status': 'INPUT', 'unit': 'GB/cm2', 'value': 1.79}


def test_verbose_component_ssd(empty_ssd_model):
    assert verbose_component(empty_ssd_model) == {'capacity': {'max': 5000.0,
                                                               'min': 100.0,
                                                               'status': 'ARCHETYPE',
                                                               'unit': 'GB',
                                                               'value': 1000.0},
                                                  'density': {'max': 1.0,
                                                              'min': 0.1,
                                                              'status': 'ARCHETYPE',
                                                              'unit': 'GB/cm2',
                                                              'value': 48.5},
                                                  'impacts': {
                                                      'adp': {'description': 'Use of minerals and fossil ressources',
                                                              'embedded': {'max': 3.2,
                                                                           'min': 0.0069,
                                                                           'significant_figures': 2,
                                                                           'value': 0.0019},
                                                              'unit': 'kgSbeq',
                                                              'use': 'not implemented'},
                                                      'gwp': {'description': 'Total climate change',
                                                              'embedded': {'max': 110000.0,
                                                                           'min': 230.0,
                                                                           'significant_figures': 2,
                                                                           'value': 52.0},
                                                              'unit': 'kgCO2eq',
                                                              'use': 'not implemented'},
                                                      'pe': {'description': 'Consumption of primary energy',
                                                             'embedded': {'max': 1370000.0,
                                                                          'min': 2810.0,
                                                                          'significant_figures': 3,
                                                                          'value': 640.0},
                                                             'unit': 'MJ',
                                                             'use': 'not implemented'}},
                                                  'units': {'max': 1.0, 'min': 1.0, 'status': 'ARCHETYPE',
                                                            'value': 1.0}}


def test_verbose_component_power_supply(empty_power_supply_model):
    assert verbose_component(empty_power_supply_model) == {
        'impacts': {'adp': {'description': 'Use of minerals and fossil ressources',
                            'embedded': {'max': 0.042,
                                         'min': 0.0083,
                                         'significant_figures': 2,
                                         'value': 0.025},
                            'unit': 'kgSbeq',
                            'use': 'not implemented'},
                    'gwp': {'description': 'Total climate change',
                            'embedded': {'max': 122.0,
                                         'min': 24.3,
                                         'significant_figures': 3,
                                         'value': 72.7},
                            'unit': 'kgCO2eq',
                            'use': 'not implemented'},
                    'pe': {'description': 'Consumption of primary energy',
                           'embedded': {'max': 1760.0,
                                        'min': 352.0,
                                        'significant_figures': 3,
                                        'value': 1050.0},
                           'unit': 'MJ',
                           'use': 'not implemented'}},
        'unit_weight': {'max': 5.0,
                        'min': 1.0,
                        'status': 'ARCHETYPE',
                        'unit': 'kg',
                        'value': 2.99},
        'units': {'max': 1.0, 'min': 1.0, 'status': 'ARCHETYPE', 'value': 1.0}}


def test_verbose_component_case(blade_case_model):
    assert verbose_component(blade_case_model) == {'case_type': {'status': 'INPUT', 'value': 'blade'},
                                                   'impacts': {
                                                       'adp': {'description': 'Use of minerals and fossil ressources',
                                                               'embedded': {'max': 0.0277,
                                                                            'min': 0.0277,
                                                                            'significant_figures': 3,
                                                                            'value': 0.0277},
                                                               'unit': 'kgSbeq',
                                                               'use': 'not implemented'},
                                                       'gwp': {'description': 'Total climate change',
                                                               'embedded': {'max': 85.9,
                                                                            'min': 85.9,
                                                                            'significant_figures': 3,
                                                                            'value': 85.9},
                                                               'unit': 'kgCO2eq',
                                                               'use': 'not implemented'},
                                                       'pe': {'description': 'Consumption of primary energy',
                                                              'embedded': {'max': 1230.0,
                                                                           'min': 1230.0,
                                                                           'significant_figures': 3,
                                                                           'value': 1230.0},
                                                              'unit': 'MJ',
                                                              'use': 'not implemented'}},
                                                   'units': {'max': 1.0, 'min': 1.0, 'status': 'ARCHETYPE',
                                                             'value': 1.0}}


def test_verbose_device_server_1(incomplete_server_model):
    verbose = verbose_device(incomplete_server_model)

    assert verbose["ASSEMBLY-1"] == {'impacts': {'adp': {'description': 'Use of minerals and fossil ressources',
                                                         'embedded': {'max': 1.41e-06,
                                                                      'min': 1.41e-06,
                                                                      'significant_figures': 3,
                                                                      'value': 1.41e-06},
                                                         'unit': 'kgSbeq',
                                                         'use': 'not implemented'},
                                                 'gwp': {'description': 'Total climate change',
                                                         'embedded': {'max': 6.68,
                                                                      'min': 6.68,
                                                                      'significant_figures': 3,
                                                                      'value': 6.68},
                                                         'unit': 'kgCO2eq',
                                                         'use': 'not implemented'},
                                                 'pe': {'description': 'Consumption of primary energy',
                                                        'embedded': {'max': 68.6,
                                                                     'min': 68.6,
                                                                     'significant_figures': 3,
                                                                     'value': 68.6},
                                                        'unit': 'MJ',
                                                        'use': 'not implemented'}},
                                     'units': {'max': 1, 'min': 1, 'status': 'ARCHETYPE', 'value': 1}}

    assert verbose["CASE-1"] == {'case_type': {'status': 'INPUT', 'value': 'rack'},
                                 'impacts': {'adp': {'description': 'Use of minerals and fossil ressources',
                                                     'embedded': {'max': 0.0202,
                                                                  'min': 0.0202,
                                                                  'significant_figures': 3,
                                                                  'value': 0.0202},
                                                     'unit': 'kgSbeq',
                                                     'use': 'not implemented'},
                                             'gwp': {'description': 'Total climate change',
                                                     'embedded': {'max': 150.0,
                                                                  'min': 150.0,
                                                                  'significant_figures': 3,
                                                                  'value': 150.0},
                                                     'unit': 'kgCO2eq',
                                                     'use': 'not implemented'},
                                             'pe': {'description': 'Consumption of primary energy',
                                                    'embedded': {'max': 2200.0,
                                                                 'min': 2200.0,
                                                                 'significant_figures': 4,
                                                                 'value': 2200.0},
                                                    'unit': 'MJ',
                                                    'use': 'not implemented'}},
                                 'units': {'max': 1.0, 'min': 1.0, 'status': 'ARCHETYPE', 'value': 1.0}}

    assert verbose["MOTHERBOARD-1"] == {'impacts': {'adp': {'description': 'Use of minerals and fossil ressources',
                                                            'embedded': {'max': 0.00369,
                                                                         'min': 0.00369,
                                                                         'significant_figures': 3,
                                                                         'value': 0.00369},
                                                            'unit': 'kgSbeq',
                                                            'use': 'not implemented'},
                                                    'gwp': {'description': 'Total climate change',
                                                            'embedded': {'max': 66.1,
                                                                         'min': 66.1,
                                                                         'significant_figures': 3,
                                                                         'value': 66.1},
                                                            'unit': 'kgCO2eq',
                                                            'use': 'not implemented'},
                                                    'pe': {'description': 'Consumption of primary energy',
                                                           'embedded': {'max': 836.0,
                                                                        'min': 836.0,
                                                                        'significant_figures': 3,
                                                                        'value': 836.0},
                                                           'unit': 'MJ',
                                                           'use': 'not implemented'}},
                                        'units': {'max': 1, 'min': 1, 'status': 'ARCHETYPE', 'value': 1}}

    assert verbose["POWER_SUPPLY-1"] == {'impacts': {'adp': {'description': 'Use of minerals and fossil ressources',
                                                             'embedded': {'max': 0.17,
                                                                          'min': 0.0083,
                                                                          'significant_figures': 2,
                                                                          'value': 0.05},
                                                             'unit': 'kgSbeq',
                                                             'use': 'not implemented'},
                                                     'gwp': {'description': 'Total climate change',
                                                             'embedded': {'max': 486.0,
                                                                          'min': 24.3,
                                                                          'significant_figures': 3,
                                                                          'value': 145.0},
                                                             'unit': 'kgCO2eq',
                                                             'use': 'not implemented'},
                                                     'pe': {'description': 'Consumption of primary energy',
                                                            'embedded': {'max': 7040.0,
                                                                         'min': 352.0,
                                                                         'significant_figures': 3,
                                                                         'value': 2100.0},
                                                            'unit': 'MJ',
                                                            'use': 'not implemented'}},
                                         'unit_weight': {'max': 5.0,
                                                         'min': 1.0,
                                                         'status': 'ARCHETYPE',
                                                         'unit': 'kg',
                                                         'value': 2.99},
                                         'units': {'max': 4.0, 'min': 1.0, 'status': 'ARCHETYPE', 'value': 2.0}}


def test_verbose_device_server_2(dell_r740_model):
    verbose = verbose_device(dell_r740_model)
    assert verbose["ASSEMBLY-1"] == {'impacts': {'adp': {'description': 'Use of minerals and fossil ressources',
                                                         'embedded': {'max': 1.41e-06,
                                                                      'min': 1.41e-06,
                                                                      'significant_figures': 3,
                                                                      'value': 1.41e-06},
                                                         'unit': 'kgSbeq',
                                                         'use': 'not implemented'},
                                                 'gwp': {'description': 'Total climate change',
                                                         'embedded': {'max': 6.68,
                                                                      'min': 6.68,
                                                                      'significant_figures': 3,
                                                                      'value': 6.68},
                                                         'unit': 'kgCO2eq',
                                                         'use': 'not implemented'},
                                                 'pe': {'description': 'Consumption of primary energy',
                                                        'embedded': {'max': 68.6,
                                                                     'min': 68.6,
                                                                     'significant_figures': 3,
                                                                     'value': 68.6},
                                                        'unit': 'MJ',
                                                        'use': 'not implemented'}},
                                     'units': {'max': 1, 'min': 1, 'status': 'ARCHETYPE', 'value': 1}}

    assert verbose["CASE-1"] == {'case_type': {'status': 'INPUT', 'value': 'rack'},
                                 'impacts': {'adp': {'description': 'Use of minerals and fossil ressources',
                                                     'embedded': {'max': 0.0202,
                                                                  'min': 0.0202,
                                                                  'significant_figures': 3,
                                                                  'value': 0.0202},
                                                     'unit': 'kgSbeq',
                                                     'use': 'not implemented'},
                                             'gwp': {'description': 'Total climate change',
                                                     'embedded': {'max': 150.0,
                                                                  'min': 150.0,
                                                                  'significant_figures': 3,
                                                                  'value': 150.0},
                                                     'unit': 'kgCO2eq',
                                                     'use': 'not implemented'},
                                             'pe': {'description': 'Consumption of primary energy',
                                                    'embedded': {'max': 2200.0,
                                                                 'min': 2200.0,
                                                                 'significant_figures': 4,
                                                                 'value': 2200.0},
                                                    'unit': 'MJ',
                                                    'use': 'not implemented'}},
                                 'units': {'max': 1.0, 'min': 1.0, 'status': 'ARCHETYPE', 'value': 1.0}}

    assert verbose["MOTHERBOARD-1"] == {'impacts': {'adp': {'description': 'Use of minerals and fossil ressources',
                                                            'embedded': {'max': 0.00369,
                                                                         'min': 0.00369,
                                                                         'significant_figures': 3,
                                                                         'value': 0.00369},
                                                            'unit': 'kgSbeq',
                                                            'use': 'not implemented'},
                                                    'gwp': {'description': 'Total climate change',
                                                            'embedded': {'max': 66.1,
                                                                         'min': 66.1,
                                                                         'significant_figures': 3,
                                                                         'value': 66.1},
                                                            'unit': 'kgCO2eq',
                                                            'use': 'not implemented'},
                                                    'pe': {'description': 'Consumption of primary energy',
                                                           'embedded': {'max': 836.0,
                                                                        'min': 836.0,
                                                                        'significant_figures': 3,
                                                                        'value': 836.0},
                                                           'unit': 'MJ',
                                                           'use': 'not implemented'}},
                                        'units': {'max': 1, 'min': 1, 'status': 'ARCHETYPE', 'value': 1}}

    assert verbose["POWER_SUPPLY-1"] == {'impacts': {'adp': {'description': 'Use of minerals and fossil ressources',
                                                             'embedded': {'max': 0.05,
                                                                          'min': 0.05,
                                                                          'significant_figures': 2,
                                                                          'value': 0.05},
                                                             'unit': 'kgSbeq',
                                                             'use': 'not implemented'},
                                                     'gwp': {'description': 'Total climate change',
                                                             'embedded': {'max': 145.0,
                                                                          'min': 145.0,
                                                                          'significant_figures': 3,
                                                                          'value': 145.0},
                                                             'unit': 'kgCO2eq',
                                                             'use': 'not implemented'},
                                                     'pe': {'description': 'Consumption of primary energy',
                                                            'embedded': {'max': 2100.0,
                                                                         'min': 2100.0,
                                                                         'significant_figures': 3,
                                                                         'value': 2100.0},
                                                            'unit': 'MJ',
                                                            'use': 'not implemented'}},
                                         'unit_weight': {'status': 'INPUT', 'unit': 'kg', 'value': 2.99},
                                         'units': {'status': 'INPUT', 'value': 2}}
