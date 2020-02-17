from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed=False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.contrib.auth.models import User, AbstractUser,AbstractBaseUser,UserManager,BaseUserManager
from django.contrib.auth.models import UserManager
from django.utils import timezone
import datetime

SERVICES_CHOICES = [('GENVZ','GENVZ'),('CALL','CALL')]
PAYMENT_CHOICES = [('CASH','CASH'),('BTC','BTC')]


class AccCdrs(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.FloatField()

    class Meta:
        
        db_table = 'acc_cdrs'


class ActiveWatchers(models.Model):
    presentity_uri = models.CharField(max_length=128)
    watcher_username = models.CharField(max_length=64)
    watcher_domain = models.CharField(max_length=64)
    to_user = models.CharField(max_length=64)
    to_domain = models.CharField(max_length=64)
    event = models.CharField(max_length=64)
    event_id = models.CharField(max_length=64, blank=True, null=True)
    to_tag = models.CharField(max_length=64)
    from_tag = models.CharField(max_length=64)
    callid = models.CharField(max_length=255)
    local_cseq = models.IntegerField()
    remote_cseq = models.IntegerField()
    contact = models.CharField(max_length=128)
    record_route = models.TextField(blank=True, null=True)
    expires = models.IntegerField()
    status = models.IntegerField()
    reason = models.CharField(max_length=64, blank=True, null=True)
    version = models.IntegerField()
    socket_info = models.CharField(max_length=64)
    local_contact = models.CharField(max_length=128)
    from_user = models.CharField(max_length=64)
    from_domain = models.CharField(max_length=64)
    updated = models.IntegerField()
    updated_winfo = models.IntegerField()
    flags = models.IntegerField()
    user_agent = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        
        db_table = 'active_watchers'
        unique_together = (('callid', 'to_tag', 'from_tag'),)


class Address(models.Model):
    grp = models.PositiveIntegerField()
    ip_addr = models.CharField(max_length=50)
    mask = models.IntegerField()
    port = models.PositiveSmallIntegerField()
    tag = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        
        db_table = 'address'


class Aliases(models.Model):
    ruid = models.CharField(unique=True, max_length=64)
    username = models.CharField(max_length=64)
    domain = models.CharField(max_length=64, blank=True, null=True)
    contact = models.CharField(max_length=255)
    received = models.CharField(max_length=128, blank=True, null=True)
    path = models.CharField(max_length=512, blank=True, null=True)
    expires = models.DateTimeField()
    q = models.FloatField()
    callid = models.CharField(max_length=255)
    cseq = models.IntegerField()
    last_modified = models.DateTimeField()
    flags = models.IntegerField()
    cflags = models.IntegerField()
    user_agent = models.CharField(max_length=255)
    socket = models.CharField(max_length=64, blank=True, null=True)
    methods = models.IntegerField(blank=True, null=True)
    instance = models.CharField(max_length=255, blank=True, null=True)
    reg_id = models.IntegerField()
    server_id = models.IntegerField()
    connection_id = models.IntegerField()
    keepalive = models.IntegerField()
    partition = models.IntegerField()

    class Meta:
        
        db_table = 'aliases'


class CarrierName(models.Model):
    carrier = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        
        db_table = 'carrier_name'


class Carrierfailureroute(models.Model):
    carrier = models.PositiveIntegerField()
    domain = models.PositiveIntegerField()
    scan_prefix = models.CharField(max_length=64)
    host_name = models.CharField(max_length=128)
    reply_code = models.CharField(max_length=3)
    flags = models.PositiveIntegerField()
    mask = models.PositiveIntegerField()
    next_domain = models.PositiveIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        
        db_table = 'carrierfailureroute'


class Carrierroute(models.Model):
    carrier = models.PositiveIntegerField()
    domain = models.PositiveIntegerField()
    scan_prefix = models.CharField(max_length=64)
    flags = models.PositiveIntegerField()
    mask = models.PositiveIntegerField()
    prob = models.FloatField()
    strip = models.PositiveIntegerField()
    rewrite_host = models.CharField(max_length=128)
    rewrite_prefix = models.CharField(max_length=64)
    rewrite_suffix = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        
        db_table = 'carrierroute'


class Cpl(models.Model):
    username = models.CharField(max_length=64)
    domain = models.CharField(max_length=64)
    cpl_xml = models.TextField(blank=True, null=True)
    cpl_bin = models.TextField(blank=True, null=True)

    class Meta:
        
        db_table = 'cpl'
        unique_together = (('username', 'domain'),)


class Dbaliases(models.Model):
    alias_username = models.CharField(max_length=64)
    alias_domain = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    domain = models.CharField(max_length=64)

    class Meta:
        
        db_table = 'dbaliases'


class Dialog(models.Model):
    hash_entry = models.PositiveIntegerField()
    hash_id = models.PositiveIntegerField()
    callid = models.CharField(max_length=255)
    from_uri = models.CharField(max_length=128)
    from_tag = models.CharField(max_length=64)
    to_uri = models.CharField(max_length=128)
    to_tag = models.CharField(max_length=64)
    caller_cseq = models.CharField(max_length=20)
    callee_cseq = models.CharField(max_length=20)
    caller_route_set = models.CharField(max_length=512, blank=True, null=True)
    callee_route_set = models.CharField(max_length=512, blank=True, null=True)
    caller_contact = models.CharField(max_length=128)
    callee_contact = models.CharField(max_length=128)
    caller_sock = models.CharField(max_length=64)
    callee_sock = models.CharField(max_length=64)
    state = models.PositiveIntegerField()
    start_time = models.PositiveIntegerField()
    timeout = models.PositiveIntegerField()
    sflags = models.PositiveIntegerField()
    iflags = models.PositiveIntegerField()
    toroute_name = models.CharField(max_length=32, blank=True, null=True)
    req_uri = models.CharField(max_length=128)
    xdata = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        
        db_table = 'dialog'


class DialogVars(models.Model):
    hash_entry = models.PositiveIntegerField()
    hash_id = models.PositiveIntegerField()
    dialog_key = models.CharField(max_length=128)
    dialog_value = models.CharField(max_length=512)

    class Meta:
        
        db_table = 'dialog_vars'


class Dialplan(models.Model):
    dpid = models.IntegerField()
    pr = models.IntegerField()
    match_op = models.IntegerField()
    match_exp = models.CharField(max_length=64)
    match_len = models.IntegerField()
    subst_exp = models.CharField(max_length=64)
    repl_exp = models.CharField(max_length=256)
    attrs = models.CharField(max_length=64)

    class Meta:
        
        db_table = 'dialplan'


class Dispatcher(models.Model):
    setid = models.IntegerField()
    destination = models.CharField(max_length=192)
    flags = models.IntegerField()
    priority = models.IntegerField()
    attrs = models.CharField(max_length=128)
    description = models.CharField(max_length=64)

    class Meta:
        
        db_table = 'dispatcher'


class Domain(models.Model):
    domain = models.CharField(unique=True, max_length=64)
    did = models.CharField(max_length=64, blank=True, null=True)
    last_modified = models.DateTimeField()

    class Meta:
        
        db_table = 'domain'


class DomainAttrs(models.Model):
    did = models.CharField(max_length=64)
    name = models.CharField(max_length=32)
    type = models.PositiveIntegerField()
    value = models.CharField(max_length=255)
    last_modified = models.DateTimeField()

    class Meta:
        
        db_table = 'domain_attrs'


class DomainName(models.Model):
    domain = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        
        db_table = 'domain_name'


class Domainpolicy(models.Model):
    rule = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    att = models.CharField(max_length=255, blank=True, null=True)
    val = models.CharField(max_length=128, blank=True, null=True)
    description = models.CharField(max_length=255)

    class Meta:
        
        db_table = 'domainpolicy'
        unique_together = (('rule', 'att', 'val'),)


class DrGateways(models.Model):
    gwid = models.AutoField(primary_key=True)
    type = models.PositiveIntegerField()
    address = models.CharField(max_length=128)
    strip = models.PositiveIntegerField()
    pri_prefix = models.CharField(max_length=64, blank=True, null=True)
    attrs = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=128)

    class Meta:
        
        db_table = 'dr_gateways'


class DrGroups(models.Model):
    username = models.CharField(max_length=64)
    domain = models.CharField(max_length=128)
    groupid = models.PositiveIntegerField()
    description = models.CharField(max_length=128)

    class Meta:
        
        db_table = 'dr_groups'


class DrGwLists(models.Model):
    gwlist = models.CharField(max_length=255)
    description = models.CharField(max_length=128)

    class Meta:
        
        db_table = 'dr_gw_lists'


class DrRules(models.Model):
    ruleid = models.AutoField(primary_key=True)
    groupid = models.CharField(max_length=255)
    prefix = models.CharField(max_length=64)
    timerec = models.CharField(max_length=255)
    priority = models.IntegerField()
    routeid = models.CharField(max_length=64)
    gwlist = models.CharField(max_length=255)
    description = models.CharField(max_length=128)

    class Meta:
        
        db_table = 'dr_rules'


class Globalblacklist(models.Model):
    prefix = models.CharField(max_length=64)
    whitelist = models.IntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        
        db_table = 'globalblacklist'


class Grp(models.Model):
    username = models.CharField(max_length=64)
    domain = models.CharField(max_length=64)
    grp = models.CharField(max_length=64)
    last_modified = models.DateTimeField()

    class Meta:
        
        db_table = 'grp'
        unique_together = (('username', 'domain', 'grp'),)


class Htable(models.Model):
    key_name = models.CharField(max_length=64)
    key_type = models.IntegerField()
    value_type = models.IntegerField()
    key_value = models.CharField(max_length=128)
    expires = models.IntegerField()

    class Meta:
        
        db_table = 'htable'


class ImcMembers(models.Model):
    username = models.CharField(max_length=64)
    domain = models.CharField(max_length=64)
    room = models.CharField(max_length=64)
    flag = models.IntegerField()

    class Meta:
        
        db_table = 'imc_members'
        unique_together = (('username', 'domain', 'room'),)


class ImcRooms(models.Model):
    name = models.CharField(max_length=64)
    domain = models.CharField(max_length=64)
    flag = models.IntegerField()

    class Meta:
        
        db_table = 'imc_rooms'
        unique_together = (('name', 'domain'),)


class LcrGw(models.Model):
    lcr_id = models.PositiveSmallIntegerField()
    gw_name = models.CharField(max_length=128, blank=True, null=True)
    ip_addr = models.CharField(max_length=50, blank=True, null=True)
    hostname = models.CharField(max_length=64, blank=True, null=True)
    port = models.PositiveSmallIntegerField(blank=True, null=True)
    params = models.CharField(max_length=64, blank=True, null=True)
    uri_scheme = models.PositiveIntegerField(blank=True, null=True)
    transport = models.PositiveIntegerField(blank=True, null=True)
    strip = models.PositiveIntegerField(blank=True, null=True)
    prefix = models.CharField(max_length=16, blank=True, null=True)
    tag = models.CharField(max_length=64, blank=True, null=True)
    flags = models.PositiveIntegerField()
    defunct = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        
        db_table = 'lcr_gw'


class LcrRule(models.Model):
    lcr_id = models.PositiveSmallIntegerField()
    prefix = models.CharField(max_length=16, blank=True, null=True)
    from_uri = models.CharField(max_length=64, blank=True, null=True)
    request_uri = models.CharField(max_length=64, blank=True, null=True)
    mt_tvalue = models.CharField(max_length=128, blank=True, null=True)
    stopper = models.PositiveIntegerField()
    enabled = models.PositiveIntegerField()

    class Meta:
        
        db_table = 'lcr_rule'
        unique_together = (('lcr_id', 'prefix', 'from_uri'),)


class LcrRuleTarget(models.Model):
    lcr_id = models.PositiveSmallIntegerField()
    rule_id = models.PositiveIntegerField()
    gw_id = models.PositiveIntegerField()
    priority = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()

    class Meta:
        
        db_table = 'lcr_rule_target'
        unique_together = (('rule_id', 'gw_id'),)


class Location(models.Model):
    ruid = models.CharField(unique=True, max_length=64)
    username = models.CharField(max_length=64)
    domain = models.CharField(max_length=64, blank=True, null=True)
    contact = models.CharField(max_length=512)
    received = models.CharField(max_length=128, blank=True, null=True)
    path = models.CharField(max_length=512, blank=True, null=True)
    expires = models.DateTimeField()
    q = models.FloatField()
    callid = models.CharField(max_length=255)
    cseq = models.IntegerField()
    last_modified = models.DateTimeField()
    flags = models.IntegerField()
    cflags = models.IntegerField()
    user_agent = models.CharField(max_length=255)
    socket = models.CharField(max_length=64, blank=True, null=True)
    methods = models.IntegerField(blank=True, null=True)
    instance = models.CharField(max_length=255, blank=True, null=True)
    reg_id = models.IntegerField()
    server_id = models.IntegerField()
    connection_id = models.IntegerField()
    keepalive = models.IntegerField()
    partition = models.IntegerField()

    class Meta:
        
        db_table = 'location'


class LocationAttrs(models.Model):
    ruid = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    domain = models.CharField(max_length=64, blank=True, null=True)
    aname = models.CharField(max_length=64)
    atype = models.IntegerField()
    avalue = models.CharField(max_length=255)
    last_modified = models.DateTimeField()

    class Meta:
        
        db_table = 'location_attrs'


class MissedCalls(models.Model):
    method = models.CharField(max_length=16)
    from_tag = models.CharField(max_length=64)
    to_tag = models.CharField(max_length=64)
    callid = models.CharField(max_length=255)
    sip_code = models.CharField(max_length=3)
    sip_reason = models.CharField(max_length=128)
    time = models.DateTimeField()

    class Meta:
        
        db_table = 'missed_calls'


class Mohqcalls(models.Model):
    mohq_id = models.PositiveIntegerField()
    call_id = models.CharField(unique=True, max_length=100)
    call_status = models.PositiveIntegerField()
    call_from = models.CharField(max_length=100)
    call_contact = models.CharField(max_length=100, blank=True, null=True)
    call_time = models.DateTimeField()

    class Meta:
        
        db_table = 'mohqcalls'


class Mohqueues(models.Model):
    name = models.CharField(unique=True, max_length=25)
    uri = models.CharField(unique=True, max_length=100)
    mohdir = models.CharField(max_length=100, blank=True, null=True)
    mohfile = models.CharField(max_length=100)
    debug = models.IntegerField()

    class Meta:
        
        db_table = 'mohqueues'


class Mtree(models.Model):
    tprefix = models.CharField(unique=True, max_length=32)
    tvalue = models.CharField(max_length=128)

    class Meta:
        
        db_table = 'mtree'


class Mtrees(models.Model):
    tname = models.CharField(max_length=128)
    tprefix = models.CharField(max_length=32)
    tvalue = models.CharField(max_length=128)

    class Meta:
        
        db_table = 'mtrees'
        unique_together = (('tname', 'tprefix', 'tvalue'),)


class Pdt(models.Model):
    sdomain = models.CharField(max_length=128)
    prefix = models.CharField(max_length=32)
    domain = models.CharField(max_length=128)

    class Meta:
        
        db_table = 'pdt'
        unique_together = (('sdomain', 'prefix'),)


class PlPipes(models.Model):
    pipeid = models.CharField(max_length=64)
    algorithm = models.CharField(max_length=32)
    plimit = models.IntegerField()

    class Meta:
        
        db_table = 'pl_pipes'


class Presentity(models.Model):
    username = models.CharField(max_length=64)
    domain = models.CharField(max_length=64)
    event = models.CharField(max_length=64)
    etag = models.CharField(max_length=64)
    expires = models.IntegerField()
    received_time = models.IntegerField()
    body = models.TextField()
    sender = models.CharField(max_length=128)
    priority = models.IntegerField()

    class Meta:
        
        db_table = 'presentity'
        unique_together = (('username', 'domain', 'event', 'etag'),)


class Pua(models.Model):
    pres_uri = models.CharField(max_length=128)
    pres_id = models.CharField(max_length=255)
    event = models.IntegerField()
    expires = models.IntegerField()
    desired_expires = models.IntegerField()
    flag = models.IntegerField()
    etag = models.CharField(max_length=64)
    tuple_id = models.CharField(max_length=64, blank=True, null=True)
    watcher_uri = models.CharField(max_length=128)
    call_id = models.CharField(max_length=255)
    to_tag = models.CharField(max_length=64)
    from_tag = models.CharField(max_length=64)
    cseq = models.IntegerField()
    record_route = models.TextField(blank=True, null=True)
    contact = models.CharField(max_length=128)
    remote_contact = models.CharField(max_length=128)
    version = models.IntegerField()
    extra_headers = models.TextField()

    class Meta:
        
        db_table = 'pua'
        unique_together = (('etag', 'tuple_id', 'call_id', 'from_tag'),)


class Purplemap(models.Model):
    sip_user = models.CharField(max_length=128)
    ext_user = models.CharField(max_length=128)
    ext_prot = models.CharField(max_length=16)
    ext_pass = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        
        db_table = 'purplemap'


class ReGrp(models.Model):
    reg_exp = models.CharField(max_length=128)
    group_id = models.IntegerField()

    class Meta:
        
        db_table = 're_grp'


class RlsPresentity(models.Model):
    rlsubs_did = models.CharField(max_length=255)
    resource_uri = models.CharField(max_length=128)
    content_type = models.CharField(max_length=255)
    presence_state = models.TextField()
    expires = models.IntegerField()
    updated = models.IntegerField()
    auth_state = models.IntegerField()
    reason = models.CharField(max_length=64)

    class Meta:
        
        db_table = 'rls_presentity'
        unique_together = (('rlsubs_did', 'resource_uri'),)


class RlsWatchers(models.Model):
    presentity_uri = models.CharField(max_length=128)
    to_user = models.CharField(max_length=64)
    to_domain = models.CharField(max_length=64)
    watcher_username = models.CharField(max_length=64)
    watcher_domain = models.CharField(max_length=64)
    event = models.CharField(max_length=64)
    event_id = models.CharField(max_length=64, blank=True, null=True)
    to_tag = models.CharField(max_length=64)
    from_tag = models.CharField(max_length=64)
    callid = models.CharField(max_length=255)
    local_cseq = models.IntegerField()
    remote_cseq = models.IntegerField()
    contact = models.CharField(max_length=128)
    record_route = models.TextField(blank=True, null=True)
    expires = models.IntegerField()
    status = models.IntegerField()
    reason = models.CharField(max_length=64)
    version = models.IntegerField()
    socket_info = models.CharField(max_length=64)
    local_contact = models.CharField(max_length=128)
    from_user = models.CharField(max_length=64)
    from_domain = models.CharField(max_length=64)
    updated = models.IntegerField()

    class Meta:
        
        db_table = 'rls_watchers'
        unique_together = (('callid', 'to_tag', 'from_tag'),)


class Rtpengine(models.Model):
    setid = models.PositiveIntegerField()
    url = models.CharField(max_length=64)
    weight = models.PositiveIntegerField()
    disabled = models.IntegerField()
    stamp = models.DateTimeField()

    class Meta:
        
        db_table = 'rtpengine'
        unique_together = (('setid', 'url'),)


class Rtpproxy(models.Model):
    setid = models.CharField(max_length=32)
    url = models.CharField(max_length=64)
    flags = models.IntegerField()
    weight = models.IntegerField()
    description = models.CharField(max_length=64)

    class Meta:
        
        db_table = 'rtpproxy'


class ScaSubscriptions(models.Model):
    subscriber = models.CharField(max_length=255)
    aor = models.CharField(max_length=255)
    event = models.IntegerField()
    expires = models.IntegerField()
    state = models.IntegerField()
    app_idx = models.IntegerField()
    call_id = models.CharField(max_length=255)
    from_tag = models.CharField(max_length=64)
    to_tag = models.CharField(max_length=64)
    record_route = models.TextField(blank=True, null=True)
    notify_cseq = models.IntegerField()
    subscribe_cseq = models.IntegerField()
    server_id = models.IntegerField()

    class Meta:
        
        db_table = 'sca_subscriptions'
        unique_together = (('subscriber', 'call_id', 'from_tag', 'to_tag'),)


class Silo(models.Model):
    src_addr = models.CharField(max_length=128)
    dst_addr = models.CharField(max_length=128)
    username = models.CharField(max_length=64)
    domain = models.CharField(max_length=64)
    inc_time = models.IntegerField()
    exp_time = models.IntegerField()
    snd_time = models.IntegerField()
    ctype = models.CharField(max_length=32)
    body = models.TextField(blank=True, null=True)
    extra_hdrs = models.TextField(blank=True, null=True)
    callid = models.CharField(max_length=128)
    status = models.IntegerField()

    class Meta:
        
        db_table = 'silo'


class SipTrace(models.Model):
    time_stamp = models.DateTimeField()
    time_us = models.PositiveIntegerField()
    callid = models.CharField(max_length=255)
    traced_user = models.CharField(max_length=128)
    msg = models.TextField()
    method = models.CharField(max_length=50)
    status = models.CharField(max_length=128)
    fromip = models.CharField(max_length=50)
    toip = models.CharField(max_length=50)
    fromtag = models.CharField(max_length=64)
    totag = models.CharField(max_length=64)
    direction = models.CharField(max_length=4)

    class Meta:
        
        db_table = 'sip_trace'


class SpeedDial(models.Model):
    username = models.CharField(max_length=64)
    domain = models.CharField(max_length=64)
    sd_username = models.CharField(max_length=64)
    sd_domain = models.CharField(max_length=64)
    new_uri = models.CharField(max_length=128)
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    description = models.CharField(max_length=64)

    class Meta:
        
        db_table = 'speed_dial'
        unique_together = (('username', 'domain', 'sd_domain', 'sd_username'),)

class Customer(AbstractUser):
    name = models.CharField(max_length=20,null=True,blank=True)
    balance = models.DecimalField(max_digits=6,decimal_places=3,null=True,blank=True,default=0)
    phoneNumber = models.CharField(max_length=10,null=True,blank=True)
    
    def __str__(self):
        if self.name:
            return self.name
        else:
            return "No identificado"
	
    @property
    def recargasHistory(self):
        return self.recarga_set.all()

    @property
    def apiUsageHistory(self):
        return self.apiusage_set.all()
    pass
    @property
    def usageHistory(self):
        return self.acc_set.all()
    @property
    def subscribers(self):
        return self.subscriber_set.all()
    pass

class Subscriber(models.Model):
    username = models.CharField(max_length=64,unique=True)
    password = models.CharField(max_length=64)
    domain = models.CharField(max_length=64,unique=True)
    ha1 = models.CharField(max_length=128)
    ha1b = models.CharField(max_length=128)
    email_address = models.CharField(max_length=128, blank=True, null=True)
    rpid = models.CharField(max_length=128, blank=True, null=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        db_table = 'subscriber'
        unique_together = (('username', 'domain'),)

    def __str__(self):
        if self.username:
            return self.username
        else:
            return "No identificado"

class Acc(models.Model):
    consumer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True,blank=True)
    method = models.CharField(max_length=16)
    from_tag = models.CharField(max_length=64)
    to_tag = models.CharField(max_length=64)
    callid = models.CharField(max_length=255)
    sip_code = models.CharField(max_length=3)
    sip_reason = models.CharField(max_length=128)
    time = models.DateTimeField()
    src_user=models.CharField(max_length=64)
    src_domain=models.CharField(max_length=128)
    src_ip =models.CharField(max_length=64)
    dst_ouser=models.CharField(max_length=64)
    dst_user =models.CharField(max_length=64)
    dst_domain =models.CharField(max_length=128)
    class Meta:
        
        db_table = 'acc'

class ApiUsage(models.Model):
	consumer = models.ForeignKey(Customer,on_delete=models.CASCADE)
	serviceProvided=models.CharField(max_length=10,choices=SERVICES_CHOICES)
	def __str__(self):
		return self.serviceProvided

class Recarga(models.Model):
	beneficiary = models.ForeignKey(Customer,on_delete=models.CASCADE)
	amount = models.DecimalField(max_digits=4,decimal_places=3)
	validated = models.BooleanField(default=False)
	methodOfPayment = models.CharField(max_length=10,choices=PAYMENT_CHOICES,default="CASH")
	def __str__(self):
		return self.amount
	pass
        


class ToposD(models.Model):
    rectime = models.DateTimeField()
    s_method = models.CharField(max_length=64)
    s_cseq = models.CharField(max_length=64)
    a_callid = models.CharField(max_length=255)
    a_uuid = models.CharField(max_length=255)
    b_uuid = models.CharField(max_length=255)
    a_contact = models.CharField(max_length=128)
    b_contact = models.CharField(max_length=128)
    as_contact = models.CharField(max_length=128)
    bs_contact = models.CharField(max_length=128)
    a_tag = models.CharField(max_length=255)
    b_tag = models.CharField(max_length=255)
    a_rr = models.TextField(blank=True, null=True)
    b_rr = models.TextField(blank=True, null=True)
    s_rr = models.TextField(blank=True, null=True)
    iflags = models.PositiveIntegerField()
    a_uri = models.CharField(max_length=128)
    b_uri = models.CharField(max_length=128)
    r_uri = models.CharField(max_length=128)
    a_srcaddr = models.CharField(max_length=128)
    b_srcaddr = models.CharField(max_length=128)
    a_socket = models.CharField(max_length=128)
    b_socket = models.CharField(max_length=128)

    class Meta:
        
        db_table = 'topos_d'


class ToposT(models.Model):
    rectime = models.DateTimeField()
    s_method = models.CharField(max_length=64)
    s_cseq = models.CharField(max_length=64)
    a_callid = models.CharField(max_length=255)
    a_uuid = models.CharField(max_length=255)
    b_uuid = models.CharField(max_length=255)
    direction = models.IntegerField()
    x_via = models.TextField(blank=True, null=True)
    x_vbranch = models.CharField(max_length=255)
    x_rr = models.TextField(blank=True, null=True)
    y_rr = models.TextField(blank=True, null=True)
    s_rr = models.TextField(blank=True, null=True)
    x_uri = models.CharField(max_length=128)
    a_contact = models.CharField(max_length=128)
    b_contact = models.CharField(max_length=128)
    as_contact = models.CharField(max_length=128)
    bs_contact = models.CharField(max_length=128)
    x_tag = models.CharField(max_length=255)
    a_tag = models.CharField(max_length=255)
    b_tag = models.CharField(max_length=255)
    a_srcaddr = models.CharField(max_length=128)
    b_srcaddr = models.CharField(max_length=128)
    a_socket = models.CharField(max_length=128)
    b_socket = models.CharField(max_length=128)

    class Meta:
        
        db_table = 'topos_t'


class Trusted(models.Model):
    src_ip = models.CharField(max_length=50)
    proto = models.CharField(max_length=4)
    from_pattern = models.CharField(max_length=64, blank=True, null=True)
    ruri_pattern = models.CharField(max_length=64, blank=True, null=True)
    tag = models.CharField(max_length=64, blank=True, null=True)
    priority = models.IntegerField()

    class Meta:
        
        db_table = 'trusted'


class Uacreg(models.Model):
    l_uuid = models.CharField(unique=True, max_length=64)
    l_username = models.CharField(max_length=64)
    l_domain = models.CharField(max_length=64)
    r_username = models.CharField(max_length=64)
    r_domain = models.CharField(max_length=64)
    realm = models.CharField(max_length=64)
    auth_username = models.CharField(max_length=64)
    auth_password = models.CharField(max_length=64)
    auth_ha1 = models.CharField(max_length=128)
    auth_proxy = models.CharField(max_length=128)
    expires = models.IntegerField()
    flags = models.IntegerField()
    reg_delay = models.IntegerField()

    class Meta:
        
        db_table = 'uacreg'


class UidCredentials(models.Model):
    auth_username = models.CharField(max_length=64)
    did = models.CharField(max_length=64)
    realm = models.CharField(max_length=64)
    password = models.CharField(max_length=28)
    flags = models.IntegerField()
    ha1 = models.CharField(max_length=32)
    ha1b = models.CharField(max_length=32)
    uid = models.CharField(max_length=64)

    class Meta:
        
        db_table = 'uid_credentials'


class UidDomain(models.Model):
    did = models.CharField(max_length=64)
    domain = models.CharField(unique=True, max_length=64)
    flags = models.PositiveIntegerField()

    class Meta:
        
        db_table = 'uid_domain'


class UidDomainAttrs(models.Model):
    did = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=32)
    type = models.IntegerField()
    value = models.CharField(max_length=128, blank=True, null=True)
    flags = models.PositiveIntegerField()

    class Meta:
        
        db_table = 'uid_domain_attrs'
        unique_together = (('did', 'name', 'value'),)


class UidGlobalAttrs(models.Model):
    name = models.CharField(max_length=32)
    type = models.IntegerField()
    value = models.CharField(max_length=128, blank=True, null=True)
    flags = models.PositiveIntegerField()

    class Meta:
        
        db_table = 'uid_global_attrs'
        unique_together = (('name', 'value'),)


class UidUri(models.Model):
    uid = models.CharField(max_length=64)
    did = models.CharField(max_length=64)
    username = models.CharField(max_length=64)
    flags = models.PositiveIntegerField()
    scheme = models.CharField(max_length=8)

    class Meta:
        
        db_table = 'uid_uri'


class UidUriAttrs(models.Model):
    username = models.CharField(max_length=64)
    did = models.CharField(max_length=64)
    name = models.CharField(max_length=32)
    value = models.CharField(max_length=128, blank=True, null=True)
    type = models.IntegerField()
    flags = models.PositiveIntegerField()
    scheme = models.CharField(max_length=8)

    class Meta:
        
        db_table = 'uid_uri_attrs'
        unique_together = (('username', 'did', 'name', 'value', 'scheme'),)


class UidUserAttrs(models.Model):
    uid = models.CharField(max_length=64)
    name = models.CharField(max_length=32)
    value = models.CharField(max_length=128, blank=True, null=True)
    type = models.IntegerField()
    flags = models.PositiveIntegerField()

    class Meta:
        
        db_table = 'uid_user_attrs'
        unique_together = (('uid', 'name', 'value'),)


class Uri(models.Model):
    username = models.CharField(max_length=64)
    domain = models.CharField(max_length=64)
    uri_user = models.CharField(max_length=64)
    last_modified = models.DateTimeField()

    class Meta:
        
        db_table = 'uri'
        unique_together = (('username', 'domain', 'uri_user'),)


class Userblacklist(models.Model):
    username = models.CharField(max_length=64)
    domain = models.CharField(max_length=64)
    prefix = models.CharField(max_length=64)
    whitelist = models.IntegerField()

    class Meta:
        
        db_table = 'userblacklist'


class UsrPreferences(models.Model):
    uuid = models.CharField(max_length=64)
    username = models.CharField(max_length=128)
    domain = models.CharField(max_length=64)
    attribute = models.CharField(max_length=32)
    type = models.IntegerField()
    value = models.CharField(max_length=128)
    last_modified = models.DateTimeField()

    class Meta:
        
        db_table = 'usr_preferences'


class Version(models.Model):
    table_name = models.CharField(unique=True, max_length=32)
    table_version = models.PositiveIntegerField()

    class Meta:
        
        db_table = 'version'


class Watchers(models.Model):
    presentity_uri = models.CharField(max_length=128)
    watcher_username = models.CharField(max_length=64)
    watcher_domain = models.CharField(max_length=64)
    event = models.CharField(max_length=64)
    status = models.IntegerField()
    reason = models.CharField(max_length=64, blank=True, null=True)
    inserted_time = models.IntegerField()

    class Meta:
        
        db_table = 'watchers'
        unique_together = (('presentity_uri', 'watcher_username', 'watcher_domain', 'event'),)


class Xcap(models.Model):
    username = models.CharField(max_length=64)
    domain = models.CharField(max_length=64)
    doc = models.TextField()
    doc_type = models.IntegerField()
    etag = models.CharField(max_length=64)
    source = models.IntegerField()
    doc_uri = models.CharField(unique=True, max_length=255)
    port = models.IntegerField()

    class Meta:
        
        db_table = 'xcap'
