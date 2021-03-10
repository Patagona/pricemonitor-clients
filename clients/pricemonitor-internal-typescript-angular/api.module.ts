import { NgModule, ModuleWithProviders, SkipSelf, Optional } from '@angular/core';
import { Configuration } from './configuration';
import { HttpClient } from '@angular/common/http';


import { AccountService } from './api/account.service';
import { CompaniesService } from './api/companies.service';
import { ControlpanelService } from './api/controlpanel.service';
import { FeedsService } from './api/feeds.service';
import { InternalService } from './api/internal.service';
import { LogsService } from './api/logs.service';
import { MonitoringSchedulesService } from './api/monitoringSchedules.service';
import { OffersService } from './api/offers.service';
import { OrdersService } from './api/orders.service';
import { PluginregistrationService } from './api/pluginregistration.service';
import { PricerecommendationsService } from './api/pricerecommendations.service';
import { ProductsService } from './api/products.service';
import { SettingsService } from './api/settings.service';
import { TasksService } from './api/tasks.service';
import { UndocumentedService } from './api/undocumented.service';

@NgModule({
  imports:      [],
  declarations: [],
  exports:      [],
  providers: []
})
export class ApiModule {
    public static forRoot(configurationFactory: () => Configuration): ModuleWithProviders<ApiModule> {
        return {
            ngModule: ApiModule,
            providers: [ { provide: Configuration, useFactory: configurationFactory } ]
        };
    }

    constructor( @Optional() @SkipSelf() parentModule: ApiModule,
                 @Optional() http: HttpClient) {
        if (parentModule) {
            throw new Error('ApiModule is already loaded. Import in your base AppModule only.');
        }
        if (!http) {
            throw new Error('You need to import the HttpClientModule in your AppModule! \n' +
            'See also https://github.com/angular/angular/issues/20575');
        }
    }
}
